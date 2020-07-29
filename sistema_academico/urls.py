"""sistema_academico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name="home"),
    path('Asistencias/', views.asistencia, name="asistencia"),
    path('Notas/', views.notas, name="notas"),
    path('Personal/', views.personal, name="personal"),
    path('Estudiantes/', views.estudiantes, name="estudiantes"),
    path('Materias/', views.materias, name="materias"),
    path('Cursos/', views.materias, name="cursos"),
    path('admin/', admin.site.urls),
]
