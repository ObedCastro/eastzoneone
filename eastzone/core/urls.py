from django.urls import path
from . import views

urlpatterns = [
    #Path's del núcleo App[core]
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
]