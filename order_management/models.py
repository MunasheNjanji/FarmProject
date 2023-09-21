from django.db import models
from django.contrib.auth.models import User
# from .user_auth.models import CustomerUser

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('product_listing.Product', through='OrderItem')
    total = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

class OrderItem(models.Model):
    order = models.ForeignKey('product_listing.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('product_listing.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    