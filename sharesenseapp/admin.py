from django.contrib import admin
from sharesenseapp.models import *
# Register your models here.
from django.contrib.auth import get_user_model
User = get_user_model()
admin.site.register(Sensor)
admin.site.register(User)