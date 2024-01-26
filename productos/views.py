from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    context={}
    return render(request, 'productos/index.html', context)

@login_required
def crud(request):
    productos = Producto.objects.all()
    context = {'productos':productos}
    return render (request, 'productos/productos_list.html', context)

