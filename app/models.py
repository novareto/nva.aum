# -*- coding: utf-8 -*-
# # Copyright (c) 2004-2020 novareto GmbH
# # lwalther@novareto.de

from typing import Optional, List, Dict, Text, Union, Literal
import datetime
from pydantic import BaseModel, Field

class NutzdatenKopfsegment(BaseModel):
    unb_2 : str = Field(u"", title=u"IK-Nummer des Absenders")
    unb_3 : Literal['12345'] = Field(u"4711", title=u"Konstante")
    unb_4 : datetime.date = Field(datetime.datetime.now().strftime('%Y-%m-%d'), title=u"Datum der Erstellung")
    unb_5 : datetime.time = Field(datetime.datetime.now().strftime('%H:%M'), title=u"Uhrzeit der Erstellung")
    unb_6 : int = Field(0, title=u"Fortlaufende Nummer des Berichts")
    unb_9 : Literal['01'] = Field(u"01", title=u"Konstante")

class UVTraeger(BaseModel):
    uvt_1 : str = Field(u"", title=u"Name des UV-Trägers")
    uvt_2 : str = Field(u"", title=u"IK-Nummer des UV-Trägers")
    uvt_3 : datetime.date = Field(datetime.datetime.now().strftime('%Y-%m-%d'), title=u"Erstellungsdatum des Berichtes")
    uvt_4 : datetime.date = Field(datetime.datetime.now().strftime('%Y-%m-%d'), title=u"Unfalltag")
    uvt_5 : Optional[str] = Field("12345678", title=u"Aktenzeichen des UV-Trägers")

class Versicherter(BaseModel):
    vin_1 : str = Field(u"", title=u"Nachname des Versicherten")
    vin_2 : str = Field(u"", title=u"Vorname des Versicherten")
    vin_3 : Optional[str] = Field(u"", title=u"Staatsangehörigkeit des Versicherten")
    vin_4 : Literal['m', 'w', 'd'] = Field(u"", title=u"Geschlecht des Versicherten")
    vin_5 : str = Field(u"", title=u"Postleitzahl des Versicherten")

class AUnfallmeldung(BaseModel):
    """
    """
    unb : NutzdatenKopfsegment
    uvt : UVTraeger
    vin : Versicherter
    
class AUnfallmeldungResponse(BaseModel):
    """
    """
    success : bool
    message : str


class EllaContact(BaseModel):
    """
    Beispiel eines Kontakt-Formulars einer ella_app.
    """
    name : Text
    vorname : Text
    subject : Text
    message : Text
    email : Text
    telefon : Optional[Text]
    mobil : Optional[Text]

class ContactResponse(BaseModel):
    """
    Antwort an die ella_app nach Versand der Kontakt-Nachricht.
    - "success" Bool-Werte true oder false
    - "message" Exception-Message bei False, Success-Message bei  true
    """
    success : bool
    message : str

