from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Crop, Inventory
from .serializers import CropSerializer, InventorySerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth.models import User
# Create your views here.

'''
here we are allowing filtering by category and name of thr product.
we are also sorting by name, unit_price and date_added'
we are goibg to be able  to search by crop name or description'
in our perform_create we are matching the current user to the crop when adding it
'''
class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'name']  
    ordering_fields = ['name', 'unit_price', 'date_added'] 
    search_fields = ['name', 'description'] 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


'''
here we only want authenticated users to perform transactions
we also match the current user to the transaction when making it
'''
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated] 
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['crop', 'transaction_type']
    ordering_fields = ['transaction_date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


'''
we are giving the admin control to list users in our project and also
to view users details
'''
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  
