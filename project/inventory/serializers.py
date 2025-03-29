from rest_framework import serializers
from .models import Crop, User,Inventory

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields='__all__'
class InventorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Inventory
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']        
