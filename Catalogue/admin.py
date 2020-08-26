from django.contrib import admin
from .models import Product_Supplier,Product_Category,Product,Product_Image,Product_Review
# Register your models here.

admin.site.register(Product_Supplier)
admin.site.register(Product_Category)
admin.site.register(Product)
admin.site.register(Product_Image)
admin.site.register(Product_Review)