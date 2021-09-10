from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zip = models.CharField(max_length=15)
    balance = models.IntegerField(default=1000)

    # def __str__(self):
    #      return self.name