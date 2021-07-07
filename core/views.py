from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedores
from .forms import ProveedorForm

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def agregar_proveedor(request):
    data ={
        'form': ProveedorForm()
    }
    
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="guardado correctamente"
        else:
            data["form"]=formulario
    
    return render(request, 'core/proveedor/agregar.html',data)

def mostrar(request):
    proveedores = Proveedores.objects.all()
    data ={
        'proveedores': proveedores
    }
    return render(request, 'core/mostrar.html',data)

def listar_proveedores(request):
    proveedores=Proveedores.objects.all()
    data ={
        'proveedores': proveedores
    }
    return render(request,'core/proveedor/listar.html',data)

def modificar_proveedor(request,id):
    
    proveedor = get_object_or_404(Proveedores, numero_id=id)
    data ={
        'form': ProveedorForm(instance=proveedor)
    }
    
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST,instance=proveedor,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to=listar_proveedores)
        data["form"] = formulario
    
    
    return render(request, 'core/proveedor/modificar.html',data)

def eliminar_proveedores(request,id):
    proveedor = get_object_or_404(Proveedores,numero_id=id)
    proveedor.delete()
    return redirect(to=listar_proveedores)