from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse('im home page')

def login(request):
        return HttpResponse('im login page')

def signup(request):
        return HttpResponse('im signup page')

# Create your views here.
