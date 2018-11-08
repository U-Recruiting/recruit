from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    mobile = models.CharField('手机号码', max_length=11)

    def __str__(self):
        return self.username
