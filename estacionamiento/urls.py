from rest_framework import routers
from .views import *
from django.urls import path

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('vehiculos', VehiculoViewSet)
router.register('espacios', EspacioViewSet)
router.register('registros', RegistroViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('vehiculos-activos/', vehiculos_activos),
]