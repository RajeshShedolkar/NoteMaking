from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from app.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    print "hello world"
    return HttpResponse("Hello, world. You're at the note-making index.")

def login(request):
    print "hello world"
    # return HttpResponse("soon login will come")
    return render(request,'login.html',{"t":"rajesh shedolkar"})

def dashboard(request):
    return render(request,'dashboard.html',{})

'''



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
