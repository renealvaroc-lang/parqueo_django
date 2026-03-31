from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Cliente, Vehiculo, Espacio, Registro
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


class EspacioViewSet(viewsets.ModelViewSet):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

@api_view(['GET'])
def vehiculos_activos(request):
    registros = Registro.objects.filter(estado='activo', fecha_salida__isnull=True)
    serializer = RegistroSerializer(registros, many=True)
    return Response(serializer.data)