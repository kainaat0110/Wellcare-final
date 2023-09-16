
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index99, name = "index99"),


]
