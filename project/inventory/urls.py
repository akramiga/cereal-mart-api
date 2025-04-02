from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, InventoryViewSet, UserRegistrationView ,  UserViewSet



router = DefaultRouter()
router.register(r'crops', CropViewSet,basename='crops')
router.register(r'transactions', InventoryViewSet, basename='transactions')
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),

]
