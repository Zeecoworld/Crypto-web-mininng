# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .activator import validate_email
# from verify_email import verify_email
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .utils import generate_ref_code
from django.urls import reverse
# Create your models here.
USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class User(AbstractUser):
    username = models.CharField(max_length=256, unique=True, blank=False,
                                validators=[
                                        RegexValidator(
                                        regex = USERNAME_REGEX,
                                        message = 'Username must be Alpahnumeric or contain any of the following: ".+ -" ',
                                        code='invalid_username'
                                        )]
                                )
    email = models.EmailField(unique=True, blank=False)
    USERNAME_FIELD = 'username' # use email to log in
   

    def __unicode__(self):
        return self.username
    

    def __str__(self):
        return self.username
    


class Referral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user")
    code = models.CharField(blank=True, max_length=8)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True ,blank=True,related_name='referred_by')
    created_by = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} ' by ' {self.recommended_by}"

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        super().save(*args,**kwargs)





    