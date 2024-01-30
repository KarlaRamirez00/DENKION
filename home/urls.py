from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index_home, name = 'index_home'),
]