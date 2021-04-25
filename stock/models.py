from django.db import models

# Create your models here.


class Stock(models.Model):
    types = models.CharField(max_length=100)

    def __str__(self):
        return self.types


class Item(models.Model):
    stock = models.ForeignKey(Stock, null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name