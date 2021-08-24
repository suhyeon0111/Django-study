from django.urls import path
from django.urls.resolvers import URLPattern

from . import views
urlpatterns=[
    path('', views.index, name = 'index'),
    path('select/', views.select, name = "select"), #기본 url에 select를 치고 들어오면 views.select가 실행됨
    path('result/', views.result, name = "result")
]