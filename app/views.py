from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from app.models import *
from django.contrib import messages
import uuid
import datetime
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
        password = request.POST['password']
        age = request.POST['age']
        test = request.POST['test']
        try :
            age = int(age)
        except:
            messages.error(request, "age shuld be number")
            return render(request,'login.html',{"t":"rajesh shedolkar"})
        user = User.objects.create_user(username=username, password=password, first_name=firstname, email=username)
        user.save()

        u = user_details(user=user, full_name=firstname, age=age, test=test)
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
    user_data = User.objects.all()
    d = []
    notes = []
    data = {'data':d,'notes':notes}
    for i in range(len(t)):
        di = {'username':user_data[i].username, 'full_name':user_data[i].first_name, 'age':t[i].age, 'test':t[i].test}
        d.append(di)
    if request.method=="POST":
        print request.POST
        notes_id = str(uuid.uuid4())
        note = request.POST['note']
        if note:
            u = NoteMaking(notes_id=notes_id, note=note)
            u.save()
            print notes_id
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
