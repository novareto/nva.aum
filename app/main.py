# -*- coding: utf-8 -*-
# # Copyright (c) 2004-2020 novareto GmbH
# # lwalther@novareto.de

from .models import AUMSingle, AUMEnvelope, AUMResponse
from .services import SiguvServices

from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse

API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"
COOKIE_DOMAIN = "localtest.me"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)

tags_metadata = [
    {
         "name": "Standard",
         "description": "Allgemeine Standard-Schnittstellen der SIGUV OpenAPI"
    },
    {
        "name": "AUM",
        "description": "Schnittstellen für die Ärztliche Unfallmeldung (AUM)"
    }
]


app = FastAPI(
    title="SIGUV OpenAPI",
    description="OpenApi für SIGUV-Online-Dienste",
    version="0.9btn (better than nothing)",
    openapi_tags = tags_metadata,
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

services = SiguvServices()

async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
    api_key_cookie: str = Security(api_key_cookie)):

    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    elif api_key_cookie == API_KEY:
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


@app.get("/", tags=["Standard"])
def read_root():
    """Willkommmen"""
    return{"message":"Herzlich Willkommen im SIGUV-Portal für die Veröffentlichung von OpenAPI-Schnittstellen"}

@app.get("/secure_endpoint", tags=["Standard"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = "How cool is this?"
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
def send_envelope_aum(api_version:str, data:AUMEnvelope):
    """
    # Übermittlung von mehrerenb Ärztlichen Unfallmeldungen in einem JSON-Array (Umschlag)

    Sie können mit folgender API-Version testen: 0.9btn (better than nothing)
    """
    if api_version == '0.9btn':
        return services.send_envolope_aum(data)
    else:
        raise HTTPException(status_code=404, detail="api_version couldn't be found")
