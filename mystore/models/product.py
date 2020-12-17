from django.db import models
from .category import Category

class Product(models.Model):
    name = models.TextField(max_length=100)
    price = models.BigIntegerField(default=0)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    stock = models.IntegerField(default=0)
    cate_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoryid')

    def __str__(self):
        self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(cate_id):
        if cate_id:
            return Product.objects.filter(cate_id=cate_id)
        else:
            return Product.get_all_products();