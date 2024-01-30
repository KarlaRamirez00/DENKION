#from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('crud_clientes', views.crud_clientes, name='crud_clientes'),
    path('clientes_add', views.clientes_ag, name='clientes_add'),
    path('clientes_edit/<str:pk>', views.clientes_edit, name='clientes_edit'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_login', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]