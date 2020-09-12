from django.contrib import admin

# Register your models here.
from .models import Product,Cart,Customer,Contact

admin.site.register(Product) 
admin.site.register(Customer) 
admin.site.register(Cart) 
admin.site.register(Contact) 