# -*- coding: utf-8 -*-
# # Copyright (c) 2004-2020 novareto GmbH
# # lwalther@novareto.de

from typing import Optional, List, Dict, Text, Union
from typing_extensions import Literal
import datetime
from pydantic import BaseModel, Field


class NutzdatenKopfsegment(BaseModel):
    """
    # Segment UNB - Nutzdaten Kopfsegment
    """
    unb_2 : str = Field(u"", title=u"IK-Nummer des Absenders")
    unb_4 : datetime.date = Field(datetime.datetime.now().strftime('%Y-%m-%d'), title=u"Datum der Erstellung")
    unb_5 : datetime.time = Field(datetime.datetime.now().strftime('%H:%M'), title=u"Uhrzeit der Erstellung")
    unb_6 : int = Field(0, title=u"Fortlaufende Nummer des Berichts")
    unb_9 : Literal['01'] = Field(u"01", title=u"Konstante")
    class Config:
        schema_extra = {
            "example" : {
                "unb_2" : "123456789",
                "unb_4" : datetime.datetime.now().strftime('%Y-%m-%d'),
                "unb_5" : datetime.datetime.now().strftime('%H:%M'),
                "unb_6" : 123,
                "unb_9" : '01',
                }
            }

class NachrichtenKopfsegment(BaseModel):
    """
    # Segment UNH - Nachrichten Kopfsegment
    """
    unh_2 : str = Field(u"AUM:20:1:01:UV", title=u"Nachrichtentyp, Versionsnummer")
    unh_3 : str = Field(u"", title=u"IK-Nummer des Empfängers")
    class Config:
        schema_extra = {
            "example" : {
                "unh_2": u"AUM:20:1:01:UV",
                "unh_3": u"120391764"
                }
            }

class UVTraeger(BaseModel):
    """
    # Segmement UVT - Unfallversicherungsträger
    """
    uvt_1 : str = Field(u"", title=u"Name des UV-Trägers")
    uvt_2 : str = Field(u"", title=u"IK-Nummer des UV-Trägers")
    uvt_3 : datetime.date = Field(datetime.datetime.now().strftime('%Y-%m-%d'), title=u"Erstellungsdatum des Berichtes")
    uvt_4 : datetime.date = Field(u"", title=u"Unfalltag")
    uvt_5 : Optional[str] = Field(u"", title=u"Aktenzeichen des UV-Trägers")
    class Config:
        schema_extra = {
            "example" : {
                "uvt_1": u"GUV Hannover",
                "uvt_2": u"120391764",
                "uvt_3": datetime.datetime.now().strftime('%Y-%m-%d'),
                "uvt_4": datetime.datetime.now().strftime('%Y-%m-%d'),
                "uvt_5": u"1234567890"
                }
            }

class Versicherter(BaseModel):
    """
    # Segment VIN - Versicherter
    """
    vin_1 : str = Field(u"", title=u"Nachname des Versicherten")
    vin_2 : str = Field(u"", title=u"Vorname des Versicherten")
    vin_3 : Optional[str] = Field(u"", title=u"Staatsangehörigkeit des Versicherten")
    vin_4 : Literal['m', 'w', 'd'] = Field(u"", title=u"Geschlecht des Versicherten")
    vin_5 : str = Field(u"", title=u"Postleitzahl des Versicherten")
    vin_6 : str = Field(u"", title=u"Ort des Versicherten")
    vin_7 : str = Field(u"", title=u"Strasse und Hausnummer des Versicherten")
    vin_8 : Optional[str] = Field(u"D", title=u"Länderkennzeichen des Wohnortes")
    vin_9 : Optional[datetime.date] = Field(u"", title=u"Geburtsdatum des Versicherten")
    vin_10 : Optional[str] = Field(u"", title=u"Telefon des Versicherten")
    vin_11 : Optional[str] = Field(u"", title=u"Versichertennummer GKV")
    class Config:
        schema_extra = {
            "example": {
                "vin_1": u"Mustermann",
                "vin_2": u"Karl",
                "vin_3": u"deutsch",
                "vin_4": u"m",
                "vin_5": u"12345",
                "vin_6": u"Hannover",
                "vin_7": u"Alleestrasse 12",
                "vin_8": u"D",
                "vin_9": u"2000-10-01",
                "vin_10": u"030 1234567890",
                "vin_11": u"AOK123445678"
                }
            }

class Unfallbetrieb(BaseModel):
    """
    # Segment UFB - Unfallbetrieb
    """
    ufb_1 : str = Field(u"", title=u"Firmenname")
    ufb_2 : Optional[str] = Field(u"D", title=u"Länderkennzeichen des Unfallbetriebes")
    ufb_3 : Optional[str] = Field(u"", title=u"Postleitzahl des Unfallbetriebes")
    ufb_4 : str = Field(u"", title=u"Ort des Unfallbetriebes")
    ufb_5 : Optional[str] = Field(u"", title=u"Strasse und Hausnummer des Unfallbetriebes")
    ufb_6 : Optional[str] = Field(u"", title=u"Beschäftigt als")
    ufb_7 : Optional[datetime.date] = Field(u"", title=u"Beschäftigt seit")
    class Config:
        schema_extra = {
            "example": {
                 "ufb_1": u"Schule für angewandte Informatik",
                 "ufb_2": u"D",
                 "ufb_3": u"12345",
                 "ufb_4": u"Hannover",
                 "ufb_5": u"Platz des Denkmals 12",
                 "ufb_6": u"Lehrer für Informatik und Religion",
                 "ufb_7": u"2010-09-01"
                 }
             }

class Kassendaten(BaseModel):
    """
    # Segment KSD - Kassendaten
    """
    ksd_1 : str = Field(u"", title=u"Krankenkasse Name")
    ksd_5 : Literal['j', 'n'] = Field(u"", title=u"Ist der Verletzte familienversichert?")
    ksd_2 : Optional[str] = Field(u"", title=u"Krankenkassen IK-Nr.")
    ksd_3 : Optional[str] = Field(u"", title=u"Pflegekasse Name")
    ksd_4 : Optional[str] = Field(u"", title=u"Pflegekasse IK-Nr.")
    class Config:
        schema_extra = {
            "example" : {
                "ksd_1": u"AOK Niedersachsen",
                "ksd_5": u"n",
                "ksd_2": u"987654321",
                "ksd_3": u"",
                "ksd_4": u"",
                }
            }

class Unfalldaten(BaseModel):
    """
    # Segment UFD - Unfalldaten
    """
    ufd_1 : Optional[str] = Field(u"", title=u"Unfallzeit")
    ufd_2 : Optional[str] = Field(u"", title=u"Arbeitszeit Beginn")
    ufd_3 : Optional[str] = Field(u"", title=u"Arbeitszeit Ende")
    class Config:
        schema_extra = {
            "example" : {
                "ufd_1": u"14:00",
                "ufd_2": u"08:00",
                "ufd_3": u"17:00"
                }
            }

class Erstbehandlung(BaseModel):
    """
    # Segment EBH - Erstbehandlung
    """
    ebh_1 : datetime.date = Field(u"", title=u"Erstbehandlung am")
    ebh_2 : str = Field(u"", title=u"Durch Arzt")
    class Config:
        schema_extra = {
            "example" : {
                "ebh_1" : datetime.datetime.now().strftime(u"%Y-%m-%d"),
                "ebh_2" : "Dr. Musterarzt"
                }
            }

class Behandlung(BaseModel):
    """
    # Segment BEH - Behandlung

    ## Beschreibung der Auswahlfelder

    ### beh_1 = Auswahl: [1,2,3,4,5]

        1 = allgemeine Behandlung
        2 = besondere Behandlung
        3 = keine Behandlung zu Lasten der ges. UV
        4 = besondere Heilbehandlung eingeleitet
        5 = besondere Heilbehandlung einleiten

    ### beh_15 = nur übermitteln, wenn beh_1 = 3

    ### beh_2 = Auswahl: [1,2]

        1 = ambulant
        2 = stationär

    ### beh_3 = Auswahl: [1,2], wenn beh_1 = 1

        1 = mich
        2 = anderen Arzt

    ### beh_14

        0 = nein
        1 = ja
    """
    beh_1 : Optional[Literal[1,2,3,4,5]] = Field(title=u"Art der Behandlung")
    beh_15 : Optional[str] = Field(u"", title=u"keine Behandlung, weil")
    beh_2 : Optional[Literal[1,2]] = Field(title=u"Behandlungstyp")
    beh_3 : Optional[Literal[1,2]] = Field(title=u"Behandlung durch")
    beh_6 : Optional[datetime.date] = Field(title=u"Nachschau, am")
    beh_7 : Optional[str] = Field(u"", title=u"Weiterbehandelnde Praxis/Krankenhaus")
    beh_8 : Optional[str] = Field(u"", title=u"Strasse Hausnummer")
    beh_9 : Optional[str] = Field(u"", title=u"PLZ")
    beh_10 : Optional[str] = Field(u"", title=u"Ort")
    beh_11 : Optional[str] = Field(u"", title=u"Länderkennzeichen")
    beh_14 : Literal[0,1] = Field(title=u"Weiterleitung an Arzt / Krankenhaus notwendig")
    class Config:
        schema_extra = {
            "example" : {
                "beh_1" : 1,
                "beh_2" : 1,
                "beh_3" : 1,
                "beh_14": 0
                }
            }

class SonstigeRechnungsinfo(BaseModel):
    """
    # Segment SRI - Sonstige Rechnungsinfo

    ## Beschreibung der Auswahlfelder

    ### sri_1 = Auswahl [1,2,3]

        1 = allgemeine
        2 = besondere
        3 = keine Behandlung zu Lasten der UV.

    ### sri_2 = Auswahl [1,2,3]

        1 = R1 (niedergel. D-Arzt/allgemein Arzt)
        2 = R2 (im Krankenhaus)
        3 = R3 (im Krankenhaus mit Besonderheiten)

    """
    sri_1 : Literal[1,2,3] = Field(title=u"Art der Heilbehandlung")
    sri_2 : Literal[1,2,3] = Field(title=u"Rechnungstyp")
    sri_4 : float = Field(title=u"Summe Gebühr")
    sri_5 : Optional[float] = Field(title=u"Summe Besondere Kosten")
    sri_6 : Optional[float] = Field(title=u"Summe Allgemeine Kosten")
    sri_7 : Optional[float] = Field(title=u"Summe Sachkosten")
    class Config:
        schema_extra = {
            "example" : {
                "sri_1" : 1,
                "sri_2" : 1,
                "sri_4" : 98.99,
                }
            }

class Rechnung(BaseModel):
    """
    # Segment REL - Rechnung

    ## Beschreibung der Auswahlfelder

    ### rel_4 = Auswahl [1,2,3]

        1 = GOÄ-Nr.
        2 = Leit-Nr. (Ärzteabkom.)
        3 = Sonstige (z.B. Fahrgeld)
    """
    rel_1 : datetime.date = Field(title=u"Leistungsdatum")
    rel_2 : float = Field(title=u"Gebühr")
    rel_3 : str = Field(u"", title=u"Leistungsposition")
    rel_4 : Literal[1,2,3] = Field(title=u"Leistungsposition Schlüssel")
    rel_5 : Optional[float] = Field(title=u"Besondere Kosten")
    rel_6 : Optional[float] = Field(title=u"Allgemeine Kosten")
    rel_7 : Optional[float] = Field(title=u"Sachkosten Kosten")
    rel_8 : Optional[str] = Field(u"", title=u"Bemerkungen")
    class Config:
        schema_extra = {
            "example" : {
                "rel_1" : datetime.datetime.now().strftime("%Y-%m-%d"),
                "rel_2" : 9.99,
                "rel_3" : u"Beratungsgespräch",
                "rel_4" : 1
                }
            }

class Konto(BaseModel):
    """
    # Segment KTO - Konto
    """
    kto_1 : float = Field(title=u"Gesamtbetrag")
    kto_2 : Optional[str] = Field(u"", title=u"Rechnungsnummer")
    kto_3 : str = Field(u"", title=u"IK des Zahlungsempfängers")
    class Config:
        schema_extra = {
            "example" : {
                "kto_1": 99.99,
                "kto_2": "DRMUSTER1234-2020",
                "kto_3": "987654321"
                }
            }

class Absender(BaseModel):
    """
    # Segment ABS - Absender
    """
    abs_1 : str = Field(title=u"Absendername")
    abs_2 : Optional[str] = Field(title=u"Strasse und Hausnummer des Absenders")
    abs_3 : Optional[str] = Field(title=u"PLZ des Absenders")
    abs_4 : str = Field(title=u"Ort des Absenders")
    abs_5 : Optional[str] = Field(title=u"Länderkennzeichen des Absenders")
    abs_6 : Optional[str] = Field(title=u"Telefon des Absenders")
    abs_7 : str = Field(title=u"Ansprechpartner des Absenders")
    class Config:
        schema_extra = {
            "example" : {
                "abs_1" : u"Orthopädische Praxis Dr. Musterarzt",
                "abs_2" : u"Distorsionsstrasse 2b",
                "abs_3" : u"51234",
                "abs_4" : u"Hannover",
                "abs_5" : u"D",
                "abs_6" : u"0511-123445678",
                "abs_7" : u"Frau Muster"
                }
            }

class AUM(BaseModel):
    """
    # Datenmodell einer Ärztlichen Unfallmeldung, basierend auf dem DALE-Standard
    """
    unh : NachrichtenKopfsegment
    uvt : UVTraeger
    vin : Versicherter
    ufb : Unfallbetrieb
    ksd : Kassendaten
    ufd : Unfalldaten
    ebh : Erstbehandlung
    beh : Behandlung
    sri : Optional[SonstigeRechnungsinfo]
    rel : Optional[List[Rechnung]]
    kto : Optional[Konto]
    abs : Absender

class AUMSingle(BaseModel):
    """
    # Datenmodell zur Übermittlung einer einzelnen Ärztlichen Unfallmeldung, basierend auf dem DALE-Standard
    """
    unb : NutzdatenKopfsegment
    aum : AUM

class AUMEnvelope(BaseModel):
    """
    # Umschlag für die Übermittlung von mehreren Ärztlichen Unfallmeldungen, basierend auf dem DALE-Standard
    """
    env : List[AUMSingle]

class AUMResponse(BaseModel):
    """
    # Modell einer Antwort der SIGUV-OpenAPI auf die Übermitttlung einer Ärztlichen Unfallmeldung
    """
    success : bool
    message : str
