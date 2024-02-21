from django.db import models
import datetime

# Category 
# Customer
# Animals
# Application

class Category(models.Model):
    name = models.CharField(max_length=70)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Animal(models.Model):
    
    CAT = 'cat'
    DOG = 'dog'
    OTHER = 'other'

    SPECIES_CHOICES = [
        (CAT, 'Кошка'),
        (DOG, 'Собака'),
        (OTHER, 'Другое'),
    ]
    
    BREED_CHOICES = [
        ('siamese', 'Сиамская'),
        ('persian', 'Персидская'),
        ('labrador', 'Лабрадор'),
        ('golden_retriever', 'Золотистый ретривер'),
    ]
    
    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]
    
    name = models.CharField(max_length=70)
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES) 
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    breed = models.CharField(max_length=50, choices=BREED_CHOICES, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image =  models.ImageField(upload_to='uploads/animal/')
    description = models.CharField(max_length=300, default='', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Application(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, default='', blank=True)
    phone = models.CharField(max_length=18, default='', blank=True)
    date = models.DateTimeField(datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.animal