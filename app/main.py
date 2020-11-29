# -*- coding: utf-8 -*-
# # Copyright (c) 2004-2020 novareto GmbH
# # lwalther@novareto.de

from .models import AUMSingle, AUMEnvelope, AUMResponse
from .services import SiguvServices
from fastapi import FastAPI
from fastapi import HTTPException

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
)
services = SiguvServices()

@app.get("/", tags=["Standard"])
def read_root():
    """Willkommmen"""
    return{"message":"Herzlich Willkommen im SIGUV-Portal für die Veröffentlichung von OpenAPI-Schnittstellen"}


@app.post("/{api_version}/single_aum", response_model=AUMResponse, tags=["AUM"])
def send_single_aum(api_version:str, data:AUMSingle):
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
