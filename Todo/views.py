from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.decorators import api_view

from rest_framework.response import Response

from Todo.models import Task
from Todo.serializers import TaskSerializer


# Create your views here.


@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List':'/task_list/',
        'Detail view':'/taskDetail/<str:pk>/',
        'name': 'samheart',
        'age' : 20,
        'sch' : 'Unn'
    }

    return Response(api_urls)




@api_view(['GET'])
def task_list(request):
    task = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(task, many=True)

    return Response(serializer.data)



@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)


@api_view(['POST' , 'GET'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)



@api_view(['POST' , 'GET'])
def taskUpdate(request, pk ):
    task = Task.objects.get(id=pk)

    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():

        serializer.save()

    # task = Task.objects.all()
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)







@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')