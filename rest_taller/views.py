from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Libro
from .serializers import LibroSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_taller(request):
    if request.method == 'GET':
        lista_taller = Libro.objects.all()
        serializer = LibroSerializer(lista_taller, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = LibroSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_taller(request, sku):
    try:
        book = Libro.objects.get(sku = sku)
    except Libro.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializ = LibroSerializer(book)
        return Response(serializ.data)
    elif request.method == "PUT":
        dataV = JSONParser().parse(request)
        serializ = LibroSerializer(book, data = dataV)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data)
        else:
            return Response(serializ.errors, status = status.HTTP_400_BAD_REQUEST) 
    elif request.method == "DELETE":
        book.delete() # DELETE A LA BD
        return Response(status = status.HTTP_204_NO_CONTENT) 


