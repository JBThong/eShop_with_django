from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=500)
    first_name = models.CharField(max_length=50, default='', blank=True)
    last_name = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.email

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if User.objects.filter(email=self.email):
            return True
        return False