from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, InventoryViewSet

router = DefaultRouter()
router.register(r'crops', CropViewSet,basename='crops')
router.register(r'transactions', InventoryViewSet, basename='transactions')

urlpatterns = [
    path('', include(router.urls)),
    

]
