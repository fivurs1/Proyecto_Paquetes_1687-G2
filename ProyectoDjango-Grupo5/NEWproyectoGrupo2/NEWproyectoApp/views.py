from django.shortcuts import render
from NEWproyectoApp.models import cliente, factura, catg_paquete, cuenta_bancaria, envios, paquete
from NEWproyectoApp.serializers import catg_paqueteSerializer, clienteSerializer, cuentaBancSerializer, enviosSerializer, facturaSerializer, paqueteSerializer
from rest_framework import serializers, viewsets

# Create your views here.
class clienteAPI(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer

class cuenta_BancAPI(viewsets.ModelViewSet):
    queryset = cuenta_bancaria.objects.all()
    serializer_class = cuentaBancSerializer

class facturaAPI(viewsets.ModelViewSet):
    queryset = factura.objects.all()
    serializer_class = facturaSerializer

class envioAPI(viewsets.ModelViewSet):
    queryset = envios.objects.all()
    serializer_class = enviosSerializer

class catg_PaqtAPI(viewsets.ModelViewSet):
    queryset = catg_paquete.objects.all()
    serializer_class = catg_paqueteSerializer

class paqueteAPI(viewsets.ModelViewSet):
    queryset = paquete.objects.all()
    serializer_class = paqueteSerializer