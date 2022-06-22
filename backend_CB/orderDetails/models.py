from django.db import models
from products.models import Product

# Create your models here.
class OrderDetail(models.Model):
  product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
  total_price = models.DecimalField(max_digits=8, decimal_places=2)
  quantity = models.IntegerField()