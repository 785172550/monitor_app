from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required


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
