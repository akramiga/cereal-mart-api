from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, InventoryViewSet, UserRegistrationView ,  UserViewSet



router = DefaultRouter()
router.register(r'crops', CropViewSet)
router.register(r'transactions', InventoryViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('inventory/summary/', CropViewSet.as_view({'get': 'inventory_summary'}), name='summary'),
]
