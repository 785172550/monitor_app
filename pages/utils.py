import requests
import json
from decimal import Decimal
from django.core.mail import send_mail
from monitor_app.settings import EMAIL_FROM
import time


def check_status(url, user):
    is_https = False
    if 'http:' not in url:
        url = 'http://' + url
    try:
        # send head request
        res = requests.head(url, allow_redirects=True)
    except:
        send_notification(url, user.sub_email, True)
        return {'status': 'DOWN', 'status_code': "No response", 'Time': 'Unknown', 'https': is_https, 'Time_number': None}
    else:
        send_notification(url, user.sub_email, False)
        time = Decimal(res.elapsed.total_seconds() * 1000).quantize(Decimal("0.00"))
        # status code >= 500 indicates there is server error, service unavailable
        # redirect to https
        if 'https' in res.url:
            is_https = True

        if res.status_code >= 500:
            return {'status': 'DOWN', 'status_code': res.status_code, 'Time': str(time) + " ms", 'https': is_https,'Time_number': time}

        # milliseconds
        return {'status': 'UP', 'status_code': res.status_code, 'Time': str(time) + " ms", 'https': is_https,'Time_number': time}


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
def send_notification(url, email, isdown):
    if (url not in urls) and isdown:
        urls[url] = time.time()
        email_title = 'Server down: ' + url
        email_body = "Email: from" + EMAIL_FROM + ', you subscribed server down: ' + url
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        return send_status
    else:
        if (url in urls) and not isdown:
            urls.pop(url)
            email_title = 'Server up: ' + url
            email_body = "Email: " + EMAIL_FROM + ', you subscribed server up: ' + url
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            return send_status
