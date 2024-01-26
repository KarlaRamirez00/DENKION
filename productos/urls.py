#from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('crud_productos', views.crud_productos, name='crud_productos'),
    path('productos_add', views.productos_ag, name='productos_add'),
]