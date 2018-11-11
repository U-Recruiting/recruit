from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Role(models.Model):
    name = models.CharField('用户角色', max_length=20, default=None)


class MyUser(AbstractUser):
    mobile = models.CharField('手机号码', max_length=11)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.username
