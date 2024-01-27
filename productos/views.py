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
    
def productos_edit(request, pk):
    if pk != "":
        producto=Producto.objects.get(id_producto=pk)
        context={'producto':producto}
        if producto:
            return render(request, 'productos/productos_edit.html', context)
        else:
            context={'mensaje':"Lo lamentamos, no existe tal producto."}
            return render(request, 'productos/productos_list.html', context)
    else:
        context={}
        return render(request, 'productos/productos_list.html', context)
    
def productosUpdate(request):
    if request.method == "POST":
        modelo=request.POST["modelo"]
        marca=request.POST["marca"]
        anno_fab=request.POST["anno_fab"]
        precio=request.POST["precio"]
        stock=request.POST["stock"]
        estado=request.POST["estado"]
        categoria=request.POST["categoria"]
        desc=request.POST["desc"]
        producto = Producto()
        producto.modelo=modelo
        producto.marca=marca
        producto.anno_fab=anno_fab
        producto.precio=precio
        producto.stock=stock
        producto.estado=estado
        producto.categoria=categoria
        producto.desc=desc
        producto.save()
        context={'mensaje':"Perfecto! Datos actualizados exitosamente", 'producto':producto}
        return render(request, 'productos/productos_list.html', context)
    else:
        productos = Producto.objects.all()
        context ={'productos':productos}
        return render(request, 'productos/productos_list.html', context)
    
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