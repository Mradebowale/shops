from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField(max_length=5000)
    category = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
    

