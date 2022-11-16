from dataclasses import field, fields
from rest_framework import serializers
from .models import cliente, cuenta_bancaria, factura, envios, catg_paquete, paquete

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ("id","TarjetaIden","nombre","apellidos","telefono","direccion","fecha_nac")

class cuentaBancSerializer(serializers.ModelSerializer):
    class Meta:
        model = cuenta_bancaria
        fields = ("id","FKcliente","num_Tarjeta","nombre")

class facturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = factura
        fields = ("id","clienteFK","nombreCliente","idFactura","fecha")

class enviosSerializer(serializers.ModelSerializer):
    class Meta:
        model = envios
        fields = ("id","FKfactura","idEnvios","cantidad","direccion")
  
class catg_paqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = catg_paquete
        fields = ("id","idCategoria","nombre")

class paqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = paquete
        fields = ("id","FKenvios","FKcategoria_paquete","idPaquete","precio")
         

