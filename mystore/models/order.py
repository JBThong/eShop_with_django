
from django.db import models
from .product import Product
from .user import User
import datetime

# order_status = types.Enum('new', 'confirmed', 'paid',
#                           'shipping', 'shipped', 'fulfilled', 'cancel',
#                           name='order_status')
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.TextField(blank=False, default='new')

class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_id')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_orderdetail_id')
    quantity = models.IntegerField(default=1)
    price = models.BigIntegerField()
    date = models.DateField(default=datetime.datetime.today)
