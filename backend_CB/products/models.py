from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
  slug = models.SlugField()
  sku = models.IntegerField()
  name = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField()
  stock = models.IntegerField()
  item_price = models.DecimalField(max_digits=8, decimal_places=2)
  
  def get_absolute_url(self):
      return reverse("products:detail", kwargs={"slug": self.slug})