
from django.urls import path
from . import views

#localhost:8000/newapp

urlpatterns = [
    path('',views.home , name='newapphome'),

]