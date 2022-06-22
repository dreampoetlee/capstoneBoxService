from django.db import models
from address.models import Address
from memberships.models import UserMembership

# Create your models here.
class Customer(models.Model):
  user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
  email = models.EmailField(max_length=255)
  password = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  first_name = models.CharField(max_length=255)

class Address(models.Model):
  address1 = models.CharField('Address line 1', max_length=255)
  address2 = models.CharField('Address line 2', max_length=255)
  zip_code = models.CharField('ZIP / Postal code', max_length=255)
  city = models.CharField('City', max_length=255)
  country = models.CharField('Country', max_length=3)
