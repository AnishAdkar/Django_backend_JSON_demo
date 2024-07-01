from django.contrib import admin
from django.urls import path
from JSON_graph_generator import views

urlpatterns = [
    path('', views.fun1, name = "Home page"),
]