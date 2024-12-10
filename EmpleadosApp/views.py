from django.shortcuts import render
from django.http import JsonResponse

# IMPORTACIONES PARA API REST
from EmpleadosApp.models import Empleado
from EmpleadosApp.serializers import EmpleadoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
def empleado(request):
    empleado = {
        'id': 1,
        'nombre': 'Juan',
        'apellido': 'Perez',
        'trabajo': 'Ingeniero'
    }
    return JsonResponse(empleado)

def empleadoV2(request):
    empleados = Empleado.objects.all() # Se obtienen todos los empleados
    data = {'empleados': list(empleados.values('nombre','apellido'))} # Se convierte en una lista de diccionarios
    return JsonResponse(data) # Se retorna la respuesta en formato JSON

@api_view(['GET','POST'])
def empleado_list(request):
    if request.method == 'GET':
        empleados = Empleado.objects.all() #Obtener todos los empleados de la DB
        serializer = EmpleadoSerializer(empleados, many=True) # Se serializan los datos
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# GET /empleadosAPI -> Obtener todos los empleados
# POST /empleadosAPI -> Crear un empleado

# GET /empleadosAPI/1 -> Obtener el empleado con id=1
# PUT /empleadosAPI/1 -> Actualizar el empleado con id=1
# DELETE /empleadosAPI/1 -> Eliminar el empleado con id=1

@api_view(['GET','PUT','DELETE'])
def empleado_detail(request, pk):
    try:
        empleado = Empleado.objects.get(pk=pk)
    except Empleado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET': 
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)
    
    if request.method = 'PUT':
        serializer = EmpleadoSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method = 'DELETE':
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)