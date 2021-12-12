from django.db import models
from django.conf import settings
# Create your models here.


User = settings.AUTH_USER_MODEL







class Newsletter(models.Model):
    email = models.EmailField(unique=True, blank=True)

