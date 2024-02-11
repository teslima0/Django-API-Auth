from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import Task, Project
from rest_framework import status
from .serializers import TaskSerializer, projectSerializer


def index(request):

    return render(request, 'index.html')



@api_view(['GET'])
def ApiOverView(request):
    api_url={
        'List': '/task-llist',

        'task-detals': '/task-detail/',
        'create':'/task-create/',
        'update':'/task-update/<str:pk>',
        'delete':'/task-delete/<str:pk>',
    }
    return Response(api_url)

@api_view(['GET'])
def Tasklist(request):
    tasks=Task.objects.all()
    serializer= TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskeDetails(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer= TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateTask(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateTask(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTask(request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()
    return Response('deleted successfully')


#============================project=============
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetAllProject(request):
    projects=Project.objects.all()
    serializer= projectSerializer(projects, many=True)
    return Response(serializer.data)

'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateProject(request):
    # Get the Profile associated with the authenticated user
    profile = Profile.objects.get(user=request.user)
    
    # Set the owner field to the Profile instance
    request.data['owner'] = profile.id
    
    serializer = projectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateProject(request):
    # Create the serializer instance with request data
    #serializer = projectSerializer(data=request.data)
     # Create the serializer instance with request data and context
    serializer = projectSerializer(data=request.data, context={'request': request})
    

    if serializer.is_valid():
        # Save the project
        serializer.save(owner=request.user.profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created object with status code 201

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if serializer is not valid

