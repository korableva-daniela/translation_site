from django.urls import path
from . import views
import os

urlpatterns = [

    path('', views.translate_app,name="trans"),
    path("upload", views.upload, name="upload")

]

