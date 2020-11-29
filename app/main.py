# -*- coding: utf-8 -*-
# # Copyright (c) 2004-2020 novareto GmbH
# # lwalther@novareto.de

from .models import EllaContact, ContactResponse, AUnfallmeldung, AUnfallmeldungResponse
from .services import SiguvServices
from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI(
    title="SIGUV OpenAPI",
    description="OpenApi für SIGUV-Online-Dienste",
    version="0.9",
)
services = SiguvServices()

@app.get("/")
def read_root():
    """Willkommmen"""
    return{"message":"Herzlich Willkommen im SIGUV-Portal für die Veröffentlichung von OpenAPI-Schnittstellen"}


@app.post("/{api_version}/contact/send", response_model=ContactResponse)
def get_data(api_version:str, data:EllaContact):
    """Die UV-Träger erhalten die Daten passend zum Kontakt-Formular. Die Daten werden
       angenommen und weitergeleitet.
    """
    if api_version == 'v09b':
        return services.send_contact_data(ella_id, data)
    else:
        raise HTTPException(status_code=404, detail="api_version couldn't be found")

@app.post("/{api_version}/aerztliche_unfallmeldung", response_model=AUnfallmeldungResponse)
def get_aerztliche_unfallmeldung(api_version:str, data:AUnfallmeldung):
    """Die UV-Träger erhalten die Daten einer ärztlichen Unfallmeldung"""
    if api_version == 'v09b':
        return services.send_unfallmeldung(data)
    else:
        raise HTTPException(status_code=404, detail="api_version couldn't be found")
