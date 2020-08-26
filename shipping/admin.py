from django.contrib import admin
from .models import Shipping_provider,Dispenser_cooler_box, Delivery

# Register your models here.
admin.site.register(Shipping_provider)
admin.site.register(Dispenser_cooler_box)
admin.site.register(Delivery)