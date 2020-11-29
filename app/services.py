# -*- coding: utf-8 -*-
# # Copyright (c) 2016-2020 educorvi GmbH & Co. KG
# # lars.walther@educorvi.de

import sys
import smtplib
import requests
from fastapi import HTTPException
#from .examples import example_apps, example_services
from .models import AUnfallmeldungResponse


class SiguvServices:

    def send_contact_data(self, ella_id, data):
        if ella_id == 'ella_example_simple':
            msg = "Nachricht von: %s %s\r\n" % (data.vorname, data.name)
            msg += data.message
            msg['Subject'] = f'The contents of {textfile}'
            msg['From'] = data.email
            msg['To'] = "your.email@domain.de"
            # Senden der Nachricht über einen SMTP-Server
            try:
                s = smtplib.SMTP('localhost')
                s.send_message(msg)
                s.quit()
                return  {'success':True, 'message': 'Die Nachricht wurde erfolgreich gesendet'}
            except:
                return  {'success':False, 'message': sys.exc_info()[0]}
        raise HTTPExeption(status_code=404, detail="ella_service not found or not allowed in this context")

    #Your service stuff after this line
    #----------------------------------

    def send_anmeldung_data(self, data):
        return AUnfallmeldungResponse(success=True, message=u'Erfolg')
