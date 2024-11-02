
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('get-sample/',sample_get_view, name='sample')
]
