from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu, name="menu"),
    path('incidentes/', views.incidentes, name="incidentes"),
    path('consultaServidor/', views.consultaServ, name="servidores"),
    path('adminIncidente/', views.adminIncidente, name="adminIncidente"),
    path('modificar/<id>/',views.modificar, name="modificar"),
    path('correo/',views.correo, name="correo"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('dashboard2/',views.dashboard2, name="dashboard2"),
    path('incidentesServ/',views.incidentesServ, name="incidentesServ"),
    path('correo2/',views.correo2, name="correo2"),
    path('modificarServ/<id>/',views.modificarServ, name="modificarServ")
]
