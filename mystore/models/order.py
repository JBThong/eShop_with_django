
from django.db import models
from .product import Product
from .user import User
import datetime

# order_status = types.Enum('new', 'confirmed', 'paid',
#                           'shipping', 'shipped', 'fulfilled', 'cancel',
#                           name='order_status')
class STATUS(models.TextChoices):
    NEW = 'new',
    CONFIRMED = 'confirmed'
    FULLFILLED = 'fulfilled'
    CANCELED = 'canceled'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.CharField(blank=False, choices=STATUS.choices, default=STATUS.NEW, max_length=20)

    @staticmethod
    def get_orders_by_user(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')

    @staticmethod
    def get_orders_by_id(id):
        return Order.objects.filter(id=id)

    @staticmethod
    def cancel_order(id):
        order = Order.objects.filter(id=id)
        for od in order:
            od.status = STATUS.CANCELED
            od.save()

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_orderdetail_id')
    quantity = models.PositiveIntegerField(default=1)
    price = models.BigIntegerField()

    @staticmethod
    def get_order_detail_by_order(order_id):
        return OrderDetail.objects.filter(order=order_id)
