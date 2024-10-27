from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_root_route(request):
    return HttpResponse("hello Django")
