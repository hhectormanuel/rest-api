
from django.contrib import admin
from django.urls import path, include

from producto.api import get

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('producto.router')),
    path("get/", get),
    

]
