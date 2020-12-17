from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def get_categories():
        return Category.objects.all()