from django.urls import path
from . import views

urlpatterns = [
    #Path's del núcleo App[church]
    path('', views.church, name="church"),
]