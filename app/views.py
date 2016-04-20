from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from app.models import *
from django.contrib import messages
import uuid
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


# def notemaking(request,id,slug):
#     # user = User.objects.create_user(username=username, password=password,
#     #                 first_name=fullname, email=email)
#     # user.save()
#     return render_to_response(request, 'dashboard.html', {})
#
# def register_user():
#     return return HttpResponseRedirect('/login')
#
# def login(request):
#     return render_to_response(request, 'dashboard.html', {})

def dashboard(request):
    t = user_details.objects.all() #getting all data from te table
    d = []
    notes = []
    data = {'data':d,'notes':notes}
    for i in t:
        di = {'username':i.username, 'full_name':i.full_name, 'age':i.age}
        d.append(di)
    if request.method=="POST":
        print request.POST
        notes_id = str(uuid.uuid4())
        note = request.POST['note']
        if note:
            u = NoteMaking(notes_id=notes_id, note=note)
            u.save()
        else:
            messages.error(request, "it's empty")
            return HttpResponseRedirect('/dashboard')
    try:
        t = NoteMaking.objects.all()
        for i in t:
                di = {'note':i.note}
                notes.append(di)
    except:
        pass
    print data
    return render(request,'dashboard.html', data)

'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
