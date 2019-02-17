import requests
import json
from decimal import Decimal


def check_status(url):
    res = ''
    if 'http:' not in url:
        url = 'http://' + url
    try:
        res = requests.head(url)
    except :
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
        return None


def encode2str(lists):
    if lists:
        content = json.dumps(lists)
        return content
    else:
        return None
