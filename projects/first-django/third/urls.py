from django.urls import path

from . import views

urlpattons = [
    path("list/", views.list, name='list'),
]