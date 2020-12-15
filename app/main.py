# -*- coding: utf-8 -*-
# # Copyright (c) 2004-2020 novareto GmbH
# # lwalther@novareto.de

import urllib.parse
from pymongo import MongoClient
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse
from .security import credentials, generic, domain
from .models import Registrierung, AUMSingle, AUMEnvelope, AUMResponse
from .services import SiguvServices

API_KEY_NAME = "access_token"
COOKIE_DOMAIN = domain

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)

username = urllib.parse.quote_plus(credentials['user'])
password = urllib.parse.quote_plus(credentials['password'])
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

tags_metadata = [
    {
         "name": "Standard",
         "description": "Allgemeine Standard-Schnittstellen der OpenAPI der UV-Kooperation"
    },
    {
        "name": "AUM",
        "description": "Schnittstellen für die Ärztliche Unfallmeldung (AUM)"
    }
]

app = FastAPI(
    title="OpenAPI der UV-Kooperation",
    description="OpenApi für Online-Dienste der UV-Kooperation",
    version="0.9btn (better than nothing)",
    openapi_tags = tags_metadata,
)

services = SiguvServices()

async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
    api_key_cookie: str = Security(api_key_cookie)):

    db = client['siguv']
    collection = db['register_collection']

    if collection.find_one({'apikey':api_key_query}):
        return api_key_query
    elif collection.find_one({'apikey':api_key_header}):
        return api_key_header
    if collection.find_one({'apikey':api_key_cookie}):
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


@app.get("/", tags=["Standard"])
def read_root():
    """Willkommmen"""
    return{"message":"Herzlich Willkommen im Portal für die Veröffentlichung von OpenAPI-Schnittstellen der UV-Kooperation"}


@app.post("/register/{gen_key}", tags=["Standard"])
def send_register_data(gen_key:str, data:Registrierung):
    """
    # Übermittlung der Regsitrierungsdaten zur Eintragung eines Kontos bei webservices.uv-kooperation.de.
    gen_key - Bitte setzen Sie sich mit uns in Verbindung, um den Schlüssel für die Kontoeröffnung zu erhalten (info@educorvi.de).
    """
    if gen_key == generic:
        return services.register_application(data)
    else:
        raise HTTPException(status_code=404, detail="api_version couldn't be found")


@app.get("/get_api_key/{checkout_key}", tags=["Standard"])
def checkout_api_key(checkout_key:str):
    """
    Service zur Aktivierung des Kontos und zum Checkout des API-Key.
    Der Aufruf des Service erfolgt über den Link in der E-Mail von webservices.uv-kooperation.de
    """
    return services.checkout_apikey(checkout_key)


@app.get("/secure_endpoint", tags=["Standard"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    """
    # Test des API-Keys
    Browseraufruf: https://webservices.uv-kooperation.de/secure_endpoint?access_token={API-Key}
    """
    response = "Der Test verlief erfolgreich."
    return response


@app.post("/{api_version}/single_aum", response_model=AUMResponse, tags=["AUM"])
def send_single_aum(api_version:str, data:AUMSingle, api_key: APIKey = Depends(get_api_key)):
    """
    # Übermittlung einer einzelnen Ärztlichen Unfallmeldung

    Sie können mit folgender API-Version testen: 0.9btn (better than nothing)
    """
    if api_version == '0.9btn':
        return services.send_single_aum(data)
    else:
        raise HTTPException(status_code=404, detail="api_version couldn't be found")


@app.post("/{api_version}/envelope_aum", response_model=AUMResponse, tags=["AUM"])
def send_envelope_aum(api_version:str, data:AUMEnvelope, api_key: APIKey = Depends(get_api_key)):
    """
    # Übermittlung von mehrerenb Ärztlichen Unfallmeldungen in einem JSON-Array (Umschlag)

    Sie können mit folgender API-Version testen: 0.9btn (better than nothing)
    """
    if api_version == '0.9btn':
        return services.send_envolope_aum(data)
    else:
        raise HTTPException(status_code=404, detail="api_version couldn't be found")
