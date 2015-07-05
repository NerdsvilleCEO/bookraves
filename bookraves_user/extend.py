from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class BookRavesUser(AbstractBaseUser):
    """
       Bookraves.org Custom User Model

       username - Defaults to email address, can be changed by user
       email_address
       oauth_token - Token used for verification of user with facebook, twitter or instagram
       full_name
       is_active - flag determining if the user is active
       last_login
       date_created
    """
    username = models.CharField(unique=True)
    date_of_birth = models.DateField()
    oauth_token = models.CharField(unique=True)
    full_name = models.CharField()
    email_address = models.CharField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'date_of_birth']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email_address
