from django.contrib.auth.models import AbstractUser
from django.db import models
from sharesenseapp.choices import DISTRICT_CHOICES

# define roles
ROLE = ((0, "regular_user"), (1, "good_people"), (2, "dispatch"))

class SenseUser(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=ROLE, default=0)
    phone = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    cam_ip = models.CharField(max_length=50, null=True,default='localhost')
    district = models.CharField(choices = DISTRICT_CHOICES, max_length=30, default=9)
    isPanic = models.BooleanField(default=False)

class Sensor (models.Model):
    name = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(SenseUser, on_delete=models.CASCADE)


