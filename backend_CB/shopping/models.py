from email.mime import image
from django.db import models

from customers.models import Customer

# Create your models here.
class Order(models.Model):
  customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
  order_details_id = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
  order_date = models.DateField()
  shipped_date = models.DateField()
  order_status = models.TextField()

class OrderDetails(models.Model):
  product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
  total_price = models.DecimalField(max_digits=8, decimal_places=2)
  quantity = models.IntegerField()

class Products(models.Model):
  sku = models.IntegerField()
  name = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField()
  stock = models.IntegerField()
