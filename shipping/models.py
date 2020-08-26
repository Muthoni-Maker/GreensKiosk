from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shipping_provider(models.Model):
    name=models.CharField(max_length=20)
    date_joined=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.IntegerField()
    transport_mode=models.CharField(max_length=30)


class Dispenser_cooler_box(models.Model):
    box_number=models.IntegerField()
    location=models.CharField(max_length=40)
    unlock_code=models.IntegerField()


class Delivery(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    dispatch_time=models.DateTimeField()
    Shipping_provider=models.ForeignKey(Order,on_delete=models.CASCADE)
    cooler_box=models.ForeignKey(Order,on_delete=models.CASCADE)





