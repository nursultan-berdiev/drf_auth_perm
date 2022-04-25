from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=255)
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Client(models.Model):
    fullname = models.CharField(max_length=255)
    date_request = models.DateField()
    request_sum = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname
