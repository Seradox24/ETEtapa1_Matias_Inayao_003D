from django.db import models

# Create your models here.

opciones_monedas=[
    [0,'Pesos'],
    [1,'Dólares']
]

class Monedas(models.Model):
    idMoneda = models.IntegerField(primary_key=True,verbose_name='id de monedas')
    nombreMoneda = models.CharField(max_length=25, verbose_name='Nombre de la moneda')
    
    def __str__(self):
        return self.nombreMoneda 

class Proveedores(models.Model):
    numero_id = models.AutoField(primary_key=True,verbose_name='Numero de Id')
    logo = models.ImageField(upload_to="proveedores",null=True,blank=True, verbose_name='imagen')
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    telefono = models.CharField(max_length=12,verbose_name='Telefono')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    email = models.EmailField(verbose_name='Email')
    pais = models.CharField(max_length=19, verbose_name='Pais')
    contraseña = models.CharField(max_length=20, verbose_name='Contraseña')
    moneda = models.ForeignKey(Monedas,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre
    
    