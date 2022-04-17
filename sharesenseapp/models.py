from django.contrib.auth.models import AbstractUser
from django.db import models
from sharesenseapp.choices import *

class SenseUser(AbstractUser):
    # define roles
    ROLE = ((0, "regular_user"), (1, "good_people"))
    role = models.PositiveSmallIntegerField(choices=ROLE, default=0)
    name = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    district = models.CharField(choices = DISTRICT_CHOICES, max_length=30, default=9)

class Sensor (models.Model):
    name = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(SenseUser, on_delete=models.CASCADE)


