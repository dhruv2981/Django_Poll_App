from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hii i am a poll page")


# Create your views here.
