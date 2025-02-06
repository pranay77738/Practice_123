from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting,Room


def welcome(request):
    return render(request,"website/welcome.html",{"meetings":Meeting.objects.all()})

def date(request):
    return HttpResponse("this page is served at"+str(datetime.now()))

def about(request):
    return HttpResponse("I am Pranay Kumar Ravula Doing Masters ")

