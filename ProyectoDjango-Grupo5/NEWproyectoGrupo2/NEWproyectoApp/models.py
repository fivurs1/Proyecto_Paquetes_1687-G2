from email.utils import format_datetime
from importlib.metadata import SelectableGroups
from lzma import FORMAT_AUTO
from typing import Iterable
from django.db import models

# Create your models here.

class cliente(models.Model):
    TarjetaIden = models.BigIntegerField()
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=150)
    fecha_nac = models.DateField()

    def __str__(self):
        return self.nombre +" "+ self.apellidos

class cuenta_bancaria(models.Model):
    FKcliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    num_Tarjeta= models.CharField(max_length=50)
    nombre = models.CharField(max_length=45)

class factura(models.Model):
    clienteFK = models.ForeignKey(cliente, on_delete= models.CASCADE)
    idFactura= models.BigIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.idFactura)
    
    def nombreCliente(self):
        return self.clienteFK.nombre+" "+self.clienteFK.apellidos
        

class envios(models.Model):
    FKfactura = models.ForeignKey(factura, on_delete= models.CASCADE)
    idEnvios = models.CharField(max_length=10)
    cantidad = models.IntegerField()
    direccion = models.CharField(max_length=150)

    def __str__(self):
        return str(self.idEnvios)

class catg_paquete(models.Model):
    idCategoria = models.CharField(max_length=10)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class paquete(models.Model):
    FKenvios = models.ForeignKey(envios, on_delete= models.CASCADE)
    FKcategoria_paquete = models.ForeignKey(catg_paquete, on_delete=models.CASCADE)
    idPaquete = models.IntegerField()
    precio = models.BigIntegerField()
