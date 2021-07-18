from store.models import category, Customer
from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
# Register your models here.
# yahan per hum apny table ko view kerwany k liye class bana rahy hain 
# or us main jo list display kerwai ha us main name wo ayain gy jo hum ny 
# product models ko create kerty howey rakhy thy
class AdminProduct(admin.ModelAdmin):
    list_display = ['Pname','proprice','category']
# uper hamari class ban rahi ha or stah main nechy usy register ker diya product k sath e
admin.site.register(Product, AdminProduct)
# yahan per hum apny table ko view kerwany k liye class bana rahy hain 
# or us main jo list display kerwai ha us main name wo ayain gy jo hum ny 
# product models ko create kerty howey rakhy thy
class AdminCategory(admin.ModelAdmin):
    list_display = ['cname']
admin.site.register(Category, AdminCategory)

# uper hamari class ban rahi ha or stah main nechy usy register ker diya Category k sath e
admin.site.register(Customer,)