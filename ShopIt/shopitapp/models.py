from django.db import models
from django.contrib.auth.models import User
# Create your models here.:



class item(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)   
    item_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    item_image = models.ImageField(upload_to='static/')
    
    class Meta:
        ordering = ['-created_on']
    
   

class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    item = models.ManyToManyField(item)
    order_date = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)