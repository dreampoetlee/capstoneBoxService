from django.db import models

# Create your models here.
class Product(models.Model):
  sku = models.IntegerField()
  name = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField()
  stock = models.IntegerField()