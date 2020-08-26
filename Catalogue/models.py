from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product_Supplier(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    street_address=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    id_number=models.IntegerField()
    date_added=models.DateField()
    profile_picture=models.ImageField()

    def __str__(self):
        return self.user.get_email()

class Product_Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    icon=models.ImageField()

    def __str__(self):
        return self.user.get_icon()

class Product(models.Model):
    title=models.CharField(max_length=20)
    
    description=models.TextField()
    supplier_price=models.DecimalField()
    selling_price=models.DecimalField()
    
    kiosk=models.ForeignKey(Kiosk,on_delete=models.CASCADE)
    number_in_stock=models.IntegerField()

    def __str__(self):
        return self.user.get_title()

class Product_Image(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField()

    def __str__(self):
        return self.user.get_product()

class Product_Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    review=models.TextField()
    score=models.IntegerField()

    def __str__(self):
        return self.user.get_customer()
