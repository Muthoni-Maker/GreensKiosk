from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=10)
    phone_number=models.IntegerField()
    date_of_birth=models.DateField()
    id_number=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.user.get_phone_number()


class Shipping_Address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    address=models.CharField(max_length=20)
    notes=models.TextField()

    def __str__(self):
        return self.user.get_address()