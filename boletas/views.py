from django.shortcuts import render, redirect
from boletas.models import Boleta
from .forms import BoletaForm
from django.contrib.auth.decorators import login_required

# Función para Listar Boletas
@login_required
def crud_boletas(request):
    boletas = Boleta.objects.all()
    context = {'boletas': boletas}
    return render(request, "boletas/boletas_list.html", context)

# Función para Agregar Boletas
@login_required
def boletas_ag(request):
    if request.method == 'POST':
        form = BoletaForm(request.POST)
        print(request.POST)  # Agrega esta línea para imprimir el contenido de request.POST
        if form.is_valid():
            form.save()
            form=BoletaForm()
            context={'mensaje':"Perfecto! La boleta se ha guardado correctamente", "form":form}
            return render(request, "boletas/boletas_add.html", context)
        else:
            print(form.errors)  # Agrega esta línea para imprimir los errores del formulario
    else:
        form = BoletaForm()
        context={'form':form}
        return render(request, "boletas/boletas_add.html", context)

# Función para Eliminar Boletas
@login_required    
def boletas_del(request, pk):
    mensajes=[]
    errores=[]
    boletas = Boleta.objects.all()
    try:
        boleta = Boleta.objects.get(id_boleta=pk)
        context={}
        if boleta:
            boleta.delete()
            mensajes.append("Perfecto! Datos eliminados")
            context = {'boletas':boletas, 'mensajes':mensajes, 'errores':errores}
            return render(request, "boletas/boletas_list.html", context)
        else:
            context={}
            return render(request, "boletas/boletas_list.html", context)
    except:
        print("Lo sentimos! No existe tal boleta")
        boletas=Boleta.objects.all()
        mensaje="Lo sentimos! No existe tal boleta"
        context={'mensaje':mensaje, 'boletas':boletas}
        return render (request, "boletas/boletas_list.html", context)

# Función 1 para Editar Boletas
@login_required    
def boletas_edit(request, pk):
    try:
        boleta = Boleta.objects.get(id_boleta=pk)
    except Boleta.DoesNotExist:
        context = {'mensaje': "Lo lamentamos, no existe tal boleta."}
        return render(request, "boletas/boletas_list.html", context)

    form = BoletaForm(instance=boleta)  # Crea una instancia del formulario con la boleta como instancia

    context = {'form': form, 'boleta': boleta}
    return render(request, "boletas/boletas_edit.html", context)

# Función 1 para Editar Boletas
@login_required
def boletasUpdate(request, pk):
    try:
        boleta = Boleta.objects.get(id_boleta=pk)
    except Boleta.DoesNotExist:
        context = {'mensaje': "Lo lamentamos, no existe tal boleta."}
        return render(request, "boletas/boletas_list.html", context)

    if request.method == "POST":
        form = BoletaForm(request.POST, instance=boleta)
        if form.is_valid():
            form.save()
            return redirect('boletas_edit', pk=pk)
    else:
        form = BoletaForm(instance=boleta)

    context = {'form': form, 'boleta': boleta}
    return render(request, "boletas/boletas_edit.html", context)