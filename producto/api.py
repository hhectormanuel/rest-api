
from rest_framework.decorators import api_view
from .serializer import ProductoSerializer
from .models import Producto
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView



@api_view(["GET", "POST"])
def get(request):
    if request.method == "GET":
        producto = Producto.objects.all()
        producto_serializer = ProductoSerializer(producto, many=True)
        return Response(producto_serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        producto_serializer = ProductoSerializer(data=request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(producto_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk=None):
    usuario = Producto.objects.get(id = pk)
    if usuario:
        if request.method == 'GET':
            
            usuario_serializer = ProductoSerializer(usuario)
            return Response(usuario_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            print('Entro al put')
            usuario_serializer = ProductoSerializer(usuario, data=request.data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response(usuario_serializer.data, status=status.HTTP_200_OK)
            return Response(usuario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProductoViewSet(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = serializer_class.Meta.model.objects.all()


class Chupeto(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer
    queryset = serializer_class.Meta.model.objects.all()
