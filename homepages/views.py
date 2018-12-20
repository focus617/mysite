from django.shortcuts import render

import datetime

# Create your views here.

def home_page(request):
    return render(request, 'homepages/index.html')

def date_time(request, offset=0):
    try:
        offset_ = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now() + datetime.timedelta(hours=offset_)
    return render(request, 'homepages/datetime.html', {"current_datetime": now})


def firstLoughe(request):
    return render(request, 'homepages/firstLoughe.html')


def newLounge(request):
    return render(request, 'homepages/newLounge.html')


def myFirstJavaScript(request):
    return render(request, 'homepages/myFirstJavaScript.html')


def json(request):
    return render(request, 'homepages/json/json.html')
