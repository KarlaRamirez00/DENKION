from django.urls import path
from . import views
from productos.views import productos_home

urlpatterns = [
    path('index', views.index_home, name = 'index_home'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('contacto', views.contacto, name = 'contacto'),
    path('co_contacto', views.co_contacto, name = 'co_contacto'),
    path('productos_home/', productos_home, name='productos_home'),

]