from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token 
from . import views

urlpatterns = [


        path('signup', views.api_signup),
        path("login/", obtain_auth_token),
        path('', views.index),
        path('create', views.create),
        path('store', views.createMovie.as_view()),
        path('show', views.showMovie.as_view()),
]