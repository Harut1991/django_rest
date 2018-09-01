from django.contrib.auth.models import AbstractUser
from django.db import models

class User( models.Model):
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'User'