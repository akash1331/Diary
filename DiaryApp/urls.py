
"""DiaryApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DiaryApp import views

urlpatterns = [

    path('',views.addentry,name = 'addentry'), #add entry url as base page
    path('addentry',views.addentry,name='addentry'), #add entry url
    path('entries',views.entries,name='entries'), #display entries url
    path('update_entry/<int:pk>',views.update_entry,name = 'update_entry'), #update entry url
    path('delete_entry/<int:pk>',views.delete_entry,name = 'delete_entry'), #delete entry url
]


