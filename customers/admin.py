from django.contrib import admin
from .models import Customer, Shipping_Address

# Register your models here.
admin.site.register(Customer)
admin.site.register(Shipping_Address)
