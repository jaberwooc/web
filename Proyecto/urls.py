"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('list/',views.list,name="list"),
    path('detail/<int:id>',views.detail, name="detail"),
    path('create/',views.create,name="create"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('list_estadios/',views.list_estadios,name="list_estadios"),
    path('create_estadios/',views.create_estadio,name="create_estadios"),
    path('delete_estadios/<int:id>',views.delete_estadio,name="delete_estadios"),
    path('detail_estadios/<int:id>',views.detail_estadio, name="detail_estadios"),
    path('update_estadios/<int:id>',views.update_estadio,name="update_estadios"),
    path('list_jugadores/',views.list_jugadores,name="list_jugadores"),
    path('create_jugadores/',views.create_jugadores,name="create_jugadores"),
    path('delete_jugadores/<int:id>',views.delete_jugadores,name="delete_jugadores"),
    path('detail_jugadores/<int:id>',views.detail_jugadores, name="detail_jugadores"),
    path('update_jugadores/<int:id>',views.update_jugadores,name="update_jugadores"),

 








]
