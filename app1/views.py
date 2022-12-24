from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def iti(request):
    return HttpResponse('<marquee>hello</marquee>')
def eno(request):
    return HttpResponse('<h2>hello there</h2')