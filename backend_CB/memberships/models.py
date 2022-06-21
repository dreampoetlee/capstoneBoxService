from django.conf import settings
from django.db import models

# Create your models here.
MEMBERSHIP_CHOICES = (
  ('Starter', 'start'),
  ('Pro', 'pro'),
  ('Premium', 'prm' )
)

class Membership(models.Model):
  slug = models.SlugField()
  membership_type = models.CharField(
    choices=MEMBERSHIP_CHOICES,
    default='Starter',
    max_length=50
  )
  price = models.DecimalField(max_digits=8, decimal_places=2)
  stripe_plan_id = models.CharField(max_length=50)

  def __str__(self):
    return self.membership_type

class UserMembership(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  stripe_customer_id = models.CharField(max_length=50)
  membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.user.username


# post_save info goes here

class Subscription(models.Model):
  user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
  stripe_subscription_id = models.CharField(max_length=50)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.user_membership.user.username