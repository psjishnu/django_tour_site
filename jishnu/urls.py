"""
from django.urls import path    
from travello import views
urlpatterns = [
    path("", views.index, name="index"),
] 
"""   
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('travello.urls')),
]
