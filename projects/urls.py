from django.urls import path
from . import views


urlpatterns = [
    path('', views.projectsUrlFunc, name="projectsPage"),
    path('project/<str:id>/', views.singleProjectPage, name="singleProjectsPage"),
]
