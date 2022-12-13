from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProfileSerializer
from .models import Profile, Projects
# Create your views here.

@api_view()
def index(request):
    return Response({'message': 'Hello world'})

@api_view()
def getProfile(request):
    try:
        profile = Profile.objects.all()[0]
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
        serializer = ProfileSerializer(projetcs, many=True)
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