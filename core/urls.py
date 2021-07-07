from django.urls import path
from .views import home,mostrar,agregar_proveedor,listar_proveedores,modificar_proveedor,eliminar_proveedores

urlpatterns = [
    path('', home, name='home'),
    path('agregar-proveedor/', agregar_proveedor, name='agregar_proveedor'),
    path('mostrar/', mostrar, name='mostrar'),
    path('listar-proveedores/',listar_proveedores,name='listar_proveedores'),
    path('modificar-proveedor/<id>/',modificar_proveedor,name='modificar_proveedor'),
    path('eliminar-proveedores/<id>/',eliminar_proveedores,name='eliminar_proveedores'),
    ]