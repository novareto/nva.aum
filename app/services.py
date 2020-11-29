# -*- coding: utf-8 -*-
# # Copyright (c) 2004-2020 novareto GmbH
# # lwalther@novareto.de

import sys
import smtplib
import requests
from fastapi import HTTPException
from .models import AUMResponse


class SiguvServices:

    def send_single_aum(self, data):
        return AUMResponse(success=True, message=u'Erfolg')

    def send_envelope_aum(self, data):
        return AUMResponse(success=True, message=u'Erfolg')
