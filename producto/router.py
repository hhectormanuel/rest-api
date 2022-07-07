from rest_framework import routers
from .api import ProductoViewSet

router = routers.DefaultRouter()
router.register(r'', ProductoViewSet, basename='Producto')

urlpatterns = router.urls
print(router.urls)

