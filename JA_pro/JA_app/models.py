from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self): return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.PROTECT, related_name='Products')
    name=models.CharField(null=True,max_length=30)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='image')
    stock=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self): return self.name

class Offer(models.Model):
    title=models.TextField(max_length=200)
    description=models.TextField(blank=True,null=True)
    discount_percentage=models.PositiveIntegerField(default=0)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="offers")
    start_date=models.DateField()
    end_date=models.DateField()

    def discounted_price(self):
        original_price = self.product.price
         
        discount =  (Decimal(self.discount_percentage / 100)) *  original_price
       
       
        return round(original_price - discount, 2)
    def __str__(self): return self.title

class ContactMessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(null=False)
    subject=models.CharField(max_length=200)
    message=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self): return self.name

    
class User(AbstractUser):
    ROLE_CHOICES=(
        ('admin','Admin'),
        ('stuff','Staff'),
        ('user','User'),

    )
    address=models.CharField(null=True, max_length=10)
    role=models.CharField(max_length=10,choices=ROLE_CHOICES, default='user')
    def __str__(self):
        return self.username




