from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index),
    path('Home/',views.index),
    path('Contact/',views.Contact),
    path('Main/',views.mainpage)
    
]