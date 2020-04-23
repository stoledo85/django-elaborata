from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime

def index(request):
    html = """<html><head></head>
    <body><h3>Este é o primeiro texto em Django.</h3>
             </body>
             </html>"""
    return HttpResponse(html)


def hora(request):
    tempoHtml = """<html><head></head><body><h3>%s</h3>
             </body>
             </html>""" % datetime.now()
    return HttpResponse(tempoHtml)