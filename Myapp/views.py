from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html' )

def About_Us(request):
    return HttpResponse("About Us")

def Contact_us(request):
    return HttpResponse("Contact_Us")
