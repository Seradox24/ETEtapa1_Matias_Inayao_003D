from django import forms
from .models import Proveedores


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores 
        #fields= '__all__'
        fields = ["nombre","telefono","direccion","email","pais","moneda","logo","numero_id",]
        
class ProveedorForm1(forms.ModelForm):
    class Meta:
        model = Proveedores 
        fields= '__all__'

