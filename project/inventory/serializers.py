from rest_framework import serializers
from .models import Crop, User,Inventory

class CropSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    current_stock = serializers.SerializerMethodField()
    class Meta:
        model = Crop
        fields = ['name','description','unit_price','added_on','last_updated','user','current_stock']
        read_only_fields = ['added_on', 'last_updated']

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



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']        


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    '''
    the validate method is going to validate our passwords to make sure they match and it returns 
    an error if they do not match
    the crate method will create a user upon sucessfull password matching
    '''
    def validate(self, password):
        if password['password1'] != password['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords  do not match!!"}
            )
        return password

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
