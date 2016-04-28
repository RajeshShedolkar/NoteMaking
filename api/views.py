from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from app.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
#from app.models import Task
from api.serializers import TaskSerializer
from api.serializers import TestSerializer
from api.serializers import NoteMakingSerializer

'''
#from rest_framework import serializers

#from app.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')
'''



# Create your views here.
def ind(request):
    return HttpResponse("hwy djdj")


@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        print request.data
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def demo(request):
    if request.method=='GET':
        tests = Test.objects.all()
        s = TestSerializer(tests, many=True)
        t = {'notes':s.data}
        return Response(t)

@api_view(['GET', 'POST'])
def note(request):
    if request.method=='GET':
        notes = NoteMaking.objects.all()
        s = NoteMakingSerializer(notes, many=True)
        return Response(s.data)
    elif request.method=='POST':
        print request.data
        serial = NoteMakingSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
