import requests
import json
from decimal import Decimal
from django.core.mail import send_mail
from monitor_app.settings import EMAIL_FROM


def check_status(url, user):
    res = ''
    if 'http:' not in url:
        url = 'http://' + url
    try:
        res = requests.head(url)
    except:
        # send_notification(url, 'sean785172550@gmail.com')
        # send_notification(url, user.email)
        return {'status': 'DOWN', 'status_code': "555", 'Time': 'Unknown'}
    else:
        time = Decimal(res.elapsed.total_seconds() * 1000).quantize(Decimal("0.00"))
        return {'status': 'UP', 'status_code': res.status_code, 'Time': str(time) + " ms"}


def decode2list(content):
    if content:
        json_dec = json.decoder.JSONDecoder()
        lists = json_dec.decode(content)
        return lists
    else:
        return []


def encode2str(lists):
    if lists:
        content = json.dumps(lists)
        return content
    else:
        return None


urls = {}

def send_notification(url, email):
    pass
    # if url not in urls:
        # urls[url] = currenttime

    #     email_title = 'server down'
    #     email_body = msg
    #     send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    #     return send_status
    # else:
        # if current time - urls[url] > 30 mins
        #     send email