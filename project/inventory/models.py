from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crop(models.Model):
    name=models.CharField(max_length=255, unique=True)
    category= models.CharField(max_length=200, blank=True, null=True)
    unit_price= models.DecimalField(max_digits=10, decimal_places=2)
    added_on=models.DateTimeField(auto_now_add=True)
    last_updated= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='crops')

class Inventory(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='transactions')
    transaction_type= models.CharField(max_length=20, choices=(('IN','Stock-in'),('OUT','Stock-out')))    
    quantity= models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)