from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print "hello world"
    return HttpResponse("Hello, world. You're at the note-making index.")

def login(request):
    print "hello world"
    return HttpResponse("soon login will come")
'''



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
