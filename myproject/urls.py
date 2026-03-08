from django.contrib import admin
from django.urls import path
from myapp import views 

urlpatterns = [
    path('admin/', admin.id),
    path('hello/', views.hello_view), 
]