from django.shortcuts import render
from django import Http
from django.http import HttpResponse
# Create your views here.

def getData(request):
    return HttpResponse("hello Django")