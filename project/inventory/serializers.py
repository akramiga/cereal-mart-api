from rest_framework import serializers
from .models import Crop,Inventory

class CropSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    current_stock = serializers.SerializerMethodField()
    class Meta:
        model = Crop
        fields = ['name','unit_price','date_added','last_updated','user','current_stock']
        read_only_fields = ['date_added', 'last_updated']

    def get_current_stock(self, obj):
        """Calculate current stock for a crop"""
        transactions = obj.transactions.all()
        stock_in = sum(
            transaction.quantity 
            for transaction in transactions 
            if transaction.transaction_type == 'IN'
        )
        stock_out = sum(
            transaction.quantity 
            for transaction in transactions 
            if transaction.transaction_type == 'OUT'
        )
        return stock_in - stock_out
    

class InventorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    crop_name = serializers.ReadOnlyField(source='crop.name')
    class Meta:
        model = Inventory
        fields = ['crop','crop_name','transaction_type', 'quantity', 'transaction_date', 'user',]
        read_only_fields = ['transaction_date']
