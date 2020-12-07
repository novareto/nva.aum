import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'mail.gmx.net'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'educorvi@gmx.de'
password = 'krks.d3print'
sender = 'educorvi@gmx.de'
targets = ['info@educorvi.de']

def send_mail(data, key):
    message = """\
Hallo %s %s,

Bitte aktivieren Sie das Konto auf webservices.uv-kooperation.de um Ihren API-Key abzurufen.
Nach Aktivierung des Kontos erhalten Sie eine E-Mail mit dem API-Key.

https://webservices.uv-kooperation.de/get_api_key/%s

Bitte informieren Sie uns, wenn Sie diese E-Mail ohne Ihr Wissen oder ohne Ihre Anforderung erhalten haben.

Ihr Team von webservices.uv-kooperation.de
""" % (data.vorname, data.name, key)
    msg = MIMEText(message)
    msg['Subject'] = u'Deine App-Registrierung für: %s (%s, %s)' % (data.application, data.name, data.vorname)
    msg['From'] = sender
    msg['To'] = data.email
    msg['Reply-to'] = 'info@educorvi.de'
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()

def checkout_mail(data):
    message = """\
Hallo %s %s,

Du bekommst hiermit den API-Key für webservices.bghw.de. Damit bist Du in der Lage, die geschützten Services von
webservices.uv-kooperation.de aufzurufen.

API-Key: %s

Für die Übermittlung des API-Keys an webservices.uv-kooperation.de können Sie wir folgt vorgehen:

- Übermittlung als Query-Parameter am Ende der URL des Webservices, https://{URL}?access_token=foo
- Übermittlung als HTTP-Header: access_token = foo

Bitte informieren Sie uns, wenn Sie diese E-Mail ohne Ihr Wissen oder ohne Ihre Anforderung erhalten haben.

Ihr Team von webservices.uv-kooperation.de
""" % (data['vorname'], data['name'], data['apikey'])
    msg = MIMEText(message)
    msg['Subject'] = u'Checkout Deines API-Keys für: %s (%s, %s)' % (data['application'], data['name'], data['vorname'])
    msg['From'] = sender
    msg['To'] = data['email']
    #msg['Reply-to'] = 'info@educorvi.de'
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()
