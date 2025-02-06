from django.shortcuts import render,get_object_or_404
from .models import Meeting,Room

def details(request,id):
    # meeting=Meeting.objects.get(pk=id)
    """This will handles the page error if user exceeds the page or not enterd an integer"""
    meeting=get_object_or_404(Meeting,pk=id)
    return render(request,"meetings/details.html",{"meeting":meeting})

def roomdet(request):

    return render(request,"meetings/roomdet.html",{"rooms": Room.objects.all()})