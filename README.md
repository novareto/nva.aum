Installation
------------

### Python-Installation (Ubuntu)

    ~/$ sudo apt-get install build-essential python-dev libjpeg-dev libxslt-dev supervisor
    ~/$ sudo apt-get install libpython3-dev
    ~/$ sudo apt-get install python3-pip

### FastApi-Installation mit nva.aum

    ~/$ git clone https://github.com/novareto/nva.aum.git
    ~/$ cd nva.aum
    ~/nva.aum$ python3 -m venv env
    ~/nva.aum$ source ./env/bin/activate
    ~/nva.aum$ pip install -r requirements.txt
    ~/nva.aum$ pip install -r dev-requirements.txt

Nach Abschluss der Installation muss im Verzeichnis "app" eine Datei security.py mit dem folgenden Inhalt
angelegt werden:

    1 credentials = {
    2     'user':"username",
    3     'password':"password"}
    4
    5 generic = "KeyFuerDenServiceZurGenerierungDesApiKeys"
    6
    7 domain = "uv-kooperation.de"

### Starten und Stoppen des API-Servers im Entwicklungsmodus

    ~/nva.aum$ uvicorn app.main:app --reload
    [CTRL-C]

Deployment für den Produktionsbetrieb
-------------------------------------

Für den Produktionsbetrieb wird eine Supervisor-Konfiguration mit einem vorgeschalteten NGINX-Server
empfohlen. Mit den folgenden Konfigurationsdateien kann eine solche Installation realisiert werden.

### Supervisor Konfiguration 

/etc/supervisor/conf.d/aum.conf

    [fcgi-program:uvicorn]
    socket=tcp://127.0.0.1:8000
    command=/home/{your_home}/nva.aum/env/bin/uvicorn --fd 0 --app-dir /home/{your_home}/nva.aum app.main:app
    numprocs=4
    process_name=uvicorn-%(process_num)d
    stdout_logfile=/dev/stdout
    stdout_logfile_maxbytes=0

### NGINX Konfiguration

/etc/nginx/sites-available/aum.conf

	upstream aum {
    	server 127.0.0.1:8000;
	}

	server {
    	server_name aum.uv-kooperation.de;
    	client_max_body_size 4G;
    	access_log /var/log/nginx/aum.de.access.log;
    	error_log /var/log/nginx/aum.de.error.log;

   		location / {
      		proxy_set_header Host $http_host;
      		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      		proxy_set_header X-Forwarded-Proto $scheme;
      		proxy_redirect off;
      		proxy_buffering off;
     		proxy_pass http://aum;
    	}


    	listen 80;

	}

Ansprechpartner / Maintainer
----------------------------

Lars Walther (lwalther@novareto.de)

Lizenz
------

FastAPI ist unter den Bedingungen der MIT lizensiert.
Urheber der Software ist Sebastian Ramirez 
E-Mail: tiangolo@gmail.com
WWW: https://tiangolo.com

Für nva.aum gelten ebenfalls die Bedingungen der MIT-Lizenz

Copyright (c) 2004-2020 novareto GmbH
lwalther@novareto.de

Weitere Quellen
---------------

- https://fastapi.tiangolo.com/
- https://dev.to/tiangolo/build-a-web-api-from-scratch-with-fastapi-the-workshop-2ehe
- https://github.com/tiangolo/blog-posts/tree/master/pyconby-web-api-from-scratch-with-fastapi/apiapp
- https://www.uvicorn.org/deployment/
