from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProfileSerializer, ProjectSerializer, SingleProjectSeralizer
from .models import Profile, Projects
import json
# Create your views here.

@api_view()
def index(request):
    return Response({'message': 'Hello world'})

@api_view()
def getProfile(request):
    try:
        profile = Profile.objects.prefetch_related('skills')[0]
        serializer = ProfileSerializer(profile)
        data = serializer.data
    except Exception as e:
        response = {
            "status": False,
            "message": f"error: {str(e)}"
        }
    else:
        response = {
            "status": True,
            "message": 'profile fetched',
            "data": data
        }
    finally:
        return Response(response)
    
@api_view()
def getProjects(request):
    try:
        projetcs = Projects.objects.all()
        serializer = ProjectSerializer(projetcs, many=True)
        data = serializer.data
    except Exception as e:
        response = {
            "status": False,
            "message": f"error: {str(e)}"
        }
    else: 
        response = {
            "status": True,
            "message": "Projects Fetched",
            "data": data
        }
    finally: 
        return Response(response)

@api_view(['GET', 'POST'])
def getProject(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            id = data["id"]
            project = Projects.objects.get(pk=id)
            serializer = SingleProjectSeralizer(project)
    except Exception as e:
        response = {
            "status": False,
            "message": f"error: {e}"
        }
    else:
        response = {
            "status": True,
            "message": "Project Fetch",
            "data": serializer.data
        }
    finally:
        return Response(response)