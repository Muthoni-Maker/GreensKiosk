from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    products=models.ManyToManyField(Products,)
    date_created=models.DateTimeField()
    total_price=models.DecimalField()
    status=models.CharField(max_length=20)


class Payment(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=10)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    amount=models.DecimalField()
    date_of_payment=models.DateTimeField()


class Order(models.Model):
    order_number=models.IntegerField()
    date_placed=models.DateTimeField()
    status=models.CharField(max_length=10)
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    delivery_time=models.DateTimeField()
    shipping_provider=models.ForeignKey(shipping_provider,on_delete=models.CASCADE)
    order_price=models.DecimalField()
    shipping_cost=models.DecimalField()
    total_price=models.DecimalField()




