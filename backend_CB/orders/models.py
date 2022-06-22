from django.db import models
from customers.models import Customer
from orderDetails.models import OrderDetail

# Create your models here.
class Order(models.Model):
  customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
  order_details_id = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
  order_date = models.DateField()
  shipped_date = models.DateField()
  order_status = models.TextField()