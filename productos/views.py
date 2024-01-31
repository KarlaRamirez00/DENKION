from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm

# Create your views here.
@login_required
def crud_productos(request):
    productos = Producto.objects.all()
    context = {'productos':productos}
    print("estoy enviando datos")
    return render(request, "productos/productos_list.html", context)

@login_required
def productos_ag(request):
    context={}

    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            print ("estoy en si es válido")
            form.save()

            #limpiar form
            form=ProductoForm()

            context={'mensaje':"Perfecto! El producto ha sido guardado correctamente", "form":form}
            return render(request, "productos/productos_add.html", context)
    else:
        form = ProductoForm()
        context = {'form':form, 'estado_choices':Producto.estado_choices}
        return render (request, 'productos/productos_add.html', context)

@login_required    
def productos_edit(request, pk):
    producto = Producto.objects.get(id_producto=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos_edit', pk=pk)
    else:
        form = ProductoForm(instance=producto)
        context = {'producto': producto, 'form': form}
        return render(request, 'productos/productos_edit.html', context)
    
@login_required    
def productos_del(request, pk):
    mensajes=[]
    errores=[]
    productos = Producto.objects.all()
    try:
        producto = Producto.objects.get(id_producto=pk)
        context={}
        if producto:
            producto.delete()
            mensajes.append("Perfecto! Datos eliminados")
            context = {'productos':productos, 'mensajes':mensajes, 'errores':errores}
            return render(request, 'productos/productos_list.html', context)
        else:
            context={}
            return render(request, 'productos/productos_list.html', context)
    except:
        print("Lo sentimos! No existe tal producto")
        productos=Producto.objects.all()
        mensaje="Lo sentimos! No existe tal producto"
        context={'mensaje':mensaje, 'productos':productos}
        return render (request, 'productos/productos_list.html', context)
    
def productos_home(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'productos/productos_home.html', context)