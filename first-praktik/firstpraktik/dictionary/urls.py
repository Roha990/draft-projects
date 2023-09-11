from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("", outpu, name="index"),
    path("add/", inpu, name="add"),
]