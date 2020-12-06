# -*- coding: utf-8 -*-
# # Copyright (c) 2004-2020 novareto GmbH
# # lwalther@novareto.de

import sys
import smtplib
import requests
import hashlib
from pymongo import MongoClient
import urllib.parse
from fastapi import HTTPException
from .models import AUMResponse
from .security import credentials

username = urllib.parse.quote_plus(credentials['user'])
password = urllib.parse.quote_plus(credentials['password'])

client = MongoClient('mongodb://%s:%s@127.0.0.1/siguv' % (username, password))

class SiguvServices:

    def register_application(self, data):
        db = client['siguv']
        collection = db['register_collection']
        m = hashlib.sha256()
        m.update(data.vorname.encode('utf-8'))
        m.update(data.name.encode('utf-8'))
        m.update(data.email.encode('utf-8'))
        m.update(data.password.encode('utf-8'))
        apikey = m.hexdigest()
        datadict = data.__dict__
        datadict['apikey'] = apikey
        post_id = collection.insert_one(datadict).inserted_id
        return {'api-key':apikey, 'id':post_id,}

    def send_single_aum(self, data):
        return AUMResponse(success=True, message=u'Erfolg')

    def send_envelope_aum(self, data):
        return AUMResponse(success=True, message=u'Erfolg')

