from django.contrib import admin
from .models import Customer, Category, Animal, Application

admin.site.register(Category)
admin.site.register(Animal)
admin.site.register(Customer)
admin.site.register(Application)
