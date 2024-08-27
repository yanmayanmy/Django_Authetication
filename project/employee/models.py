from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
class MemberManager(BaseUserManager):
    pass

class Employee(AbstractBaseUser):
    e_id = models.CharField(primary_key=True, max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'e_id'
    objects = MemberManager()