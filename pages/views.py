from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .utils import check_status, decode2list
import time

# to record response time about each requets
response_time = {}


# Create your views here.

@login_required
def index(request):
    user = request.user
    jsonDec = json.decoder.JSONDecoder()
    if user.myList:
        urls = jsonDec.decode(user.myList)
    else:
        urls = []
    return render(request, 'index.html', {'urls': urls})


def blank(request):
    return render(request, 'blank.html')


def settings(request):
    return render(request, 'settings.html')


def data_fresh(request):
    user = request.user
    urls = decode2list(user.myList)
    res = {}
    if urls is None:
        return JsonResponse(res)
    for url in urls:
        res[url] = check_status(url, user)

    response_time[time.time()] = res
    return JsonResponse(res)


def response_timemap(request):
    return JsonResponse(response_time)


def check_http():
    pass
