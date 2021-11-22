from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, phone, password, **other_fields):
        if not username:
            raise ValueError('Username is required!')
        elif not phone:
            raise ValueError('Phone number is required!')

        username = self.model.normalize_username(username)
        user = self.model(username=username, phone=phone, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, phone, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(username, first_name, last_name, phone, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=15, unique=True, primary_key=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)
    is_expart = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']
    objects = CustomUserManager()


    def __str__(self) -> str:
        return self.username