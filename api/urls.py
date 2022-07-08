
from django.contrib import admin
from django.urls import path, include

from producto.api import get, usuario_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('producto.router')),
    path("get/", get),
    path("delete/<int:pk>", usuario_detail)
    

]
