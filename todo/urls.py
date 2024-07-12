from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path("",views.home, name="home"),
    path("create/",views.create, name="create"),
    path('complete/<int:todo_id>/', views.complete, name='complete'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    
]