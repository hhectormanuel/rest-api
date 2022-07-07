
from rest_framework.decorators import api_view
from .serializer import ProductoSerializer
from .models import Producto
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet



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


class ProductoViewSet(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = serializer_class.Meta.model.objects.all()
