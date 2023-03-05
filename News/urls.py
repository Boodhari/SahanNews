from django.contrib import admin
from django.urls import path
from News.views import Homeview

urlpatterns = [
    path('',Homeview , name='home'),
]