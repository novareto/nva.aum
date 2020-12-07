# -*- coding: utf-8 -*-
# # Copyright (c) 2004-2020 novareto GmbH
# # lwalther@novareto.de

import sys
import smtplib
import requests
import hashlib
from bson.objectid import ObjectId
from pymongo import MongoClient
import urllib.parse
from fastapi import HTTPException
from .models import AUMResponse
from .security import credentials
from .sendmail import send_mail, checkout_mail

username = urllib.parse.quote_plus(credentials['user'])
password = urllib.parse.quote_plus(credentials['password'])
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

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
        send = send_mail(data, str(post_id))
        return {'status':'success', 'message':'Bitte achten Sie auf die E-Mail zur Aktivierung Ihres Kontos'}

    def checkout_apikey(self, checkout_key):
        db = client['siguv']
        collection = db['register_collection']
        post_id = ObjectId(checkout_key)
        data = collection.find_one({"_id": post_id})
        send = checkout_mail(data)
        return {'status':'success', 'message':'Bitte achten Sie auf die E-Mail mit dem Checkout des API-Key'}

    def send_single_aum(self, data):
        return AUMResponse(success=True, message=u'Erfolg')

    def send_envelope_aum(self, data):
        return AUMResponse(success=True, message=u'Erfolg')

