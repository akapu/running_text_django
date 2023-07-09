from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("runtext", views.video, name="video"),
]
