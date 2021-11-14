from django import http
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='color:red'> Hello World </h1>")