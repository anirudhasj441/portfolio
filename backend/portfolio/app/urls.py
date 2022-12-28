from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('get_profile/', views.getProfile),
    path('get_projects/', views.getProjects),
    path('get_project/', views.getProject),
]