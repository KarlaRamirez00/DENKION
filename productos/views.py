from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm

# Create your views here.
def crud_productos(request):
    productos = Producto.objects.all()
    context = {'productos':productos}
    print("estoy enviando datos")
    return render(request, "productos/productos_list.html", context)

def productos_ag(request):
    context={}

    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid:
            print ("estoy en si es válido")
            form.save()

            #limpiar form
            form=ProductoForm()

            context={'mensaje':"Perfecto! El producto ha sido guardado correctamente", "form":form}
            return render(request, "productos/productos_add.html", context)
    else:
        form = ProductoForm()
        context = {'form':form}
        return render (request, 'productos/productos_add.html', context)