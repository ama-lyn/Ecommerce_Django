from django.db import models

# Create your models here.
# Just a table 
class Product(models.Model):
    name= models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    
    
class Details(models.Model):
    pass
    
# How Django works     
# MVT
# MVu(appurl) -> (projurl) T
# Model, View , URLS, Template