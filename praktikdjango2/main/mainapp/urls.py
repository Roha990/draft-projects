from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("reg/", reg_page),
    path("login/", log_page),
    path("note/", note),
    path("note/add", add),
    path("lg", logout_page),
]