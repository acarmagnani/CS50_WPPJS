from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    path("<str:name>" , views.greet , name="freet"),
    path("antonio" , views.antonio , name="antonio")
]