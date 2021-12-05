from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu, name="menu"),
    path('incidentes/', views.incidentes, name="incidentes"),
    path('consultaServidor/', views.consultaServ, name="servidores"),
]
