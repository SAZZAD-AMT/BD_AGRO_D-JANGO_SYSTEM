from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



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
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='user.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()