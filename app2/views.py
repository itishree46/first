from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ss(request):
    return HttpResponse('<marquee><h1>welcome to hell</h1></marquee>')
def kk(request):
    return HttpResponse('<h2>hello helo</h2>')