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
    if request.method=='GET':
        return render(request,'login.html',{"t":"rajesh shedolkar"})
    else :
        print request.POST
        username = request.POST['username']
        firstname = request.POST['firstname']
        age = request.POST['age']
        try :
            age = int(age)
        except:
            messages.error(request, "age shuld be number")
            return render(request,'login.html',{"t":"rajesh shedolkar"})
        u = user_details(full_name=firstname, username=username, age=age)
        u.save()
        return HttpResponseRedirect('/dashboard')

def dashboard(request):
    return render(request,'dashboard.html', data)

'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
