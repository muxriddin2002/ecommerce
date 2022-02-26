from django.db import models
from django.contrib.auth.models import User,AbstractUser


class Customer(AbstractUser):
    adress = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.PositiveBigIntegerField(blank=True, null=True)
