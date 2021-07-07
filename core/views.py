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
            id=Proveedores.objects.last()
            
            extrac1 = id.numero_id
            extrac1 = int(extrac1)+1
            extrac2 = formulario.cleaned_data['nombre']
            extrac3 = formulario.cleaned_data['pais']
            extrac4 = formulario.cleaned_data['telefono']
            genpass =  str(extrac1)[0:2]+str(extrac2.upper())[0:2]+ str(extrac3.lower())[-2:]+str(extrac4)[-2:]
            
            #print("nombre: "+ str(extrac1))
            print (str(id.numero_id))
            print(extrac1)
            print("nombre: "+ str(extrac2))
            print("nombre: "+ str(extrac3))
            print("nombre: "+ str(extrac4))
            print("nombre: "+ str(genpass))
            formulario = Proveedores(
                nombre =formulario.cleaned_data['nombre'],
                telefono =formulario.cleaned_data['telefono'],
                direccion =formulario.cleaned_data['direccion'],
                email =formulario.cleaned_data['email'],
                pais =formulario.cleaned_data['pais'],
                moneda =formulario.cleaned_data['moneda'],
                logo =formulario.cleaned_data['logo'],
                contraseña = genpass,
                
            )
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