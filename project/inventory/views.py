from django.shortcuts import render
from rest_framework import viewsets, permissions,generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.views import APIView
from .models import Crop, Inventory
from .serializers import CropSerializer, InventorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsOwnerOrReadOnly

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
    search_fields = ['name'] 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def inventory_summary(self, request):
        """
        Provide a summary of inventory levels for all crops
        """
        summary = []
        for crop in Crop.objects.all():
            stock_in = crop.transactions.filter(transaction_type='IN').aggregate(
                total_in=Sum('quantity')
            )['total_in'] or 0
            
            stock_out = crop.transactions.filter(transaction_type='OUT').aggregate(
                total_out=Sum('quantity')
            )['total_out'] or 0
            
            current_stock = stock_in - stock_out
            
            summary.append({
                'crop_name': crop.name,
                'current_stock': current_stock,
                'unit_price': crop.unit_price,
                'category': crop.category
            })
        
        return Response(summary)
    


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



