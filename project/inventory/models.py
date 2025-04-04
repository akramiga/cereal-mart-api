from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crop(models.Model):
    name=models.CharField(max_length=255, unique=True)
    category= models.CharField(max_length=200, blank=True, null=True)
    unit_price= models.DecimalField(max_digits=10, decimal_places=2)
    date_added=models.DateTimeField(auto_now_add=True)
    last_updated= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete= models.PROTECT, related_name='crops')
    def __str__(self):
        return f'{self.name} ({self.category})'

class Inventory(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.PROTECT, related_name='transactions')
    transaction_type= models.CharField(max_length=20, choices=(('IN','Stock-in'),('OUT','Stock-out')))    
    quantity= models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    transaction_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.crop} ({self.transaction_type}) - {self.quantity}'
        