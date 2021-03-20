from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    #path('movie/',include('movie.urls'))
    path('index', views.index, name='index'),
    path('create',views.create,name='create'),
    path('show/<int:id>',views.show,name='show'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),


]