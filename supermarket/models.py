from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.utils.timezone import now
from .managers import CustomUserManager




    
class User(AbstractUser, PermissionsMixin):
    pass
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    password = models.CharField(max_length=128, verbose_name='password')
    last_login= models.DateTimeField(blank=True, null=True, verbose_name='last login')
    is_superuser = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    first_name = models.CharField(blank=True, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=150, verbose_name='last name')
    is_staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    is_active = models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    date_joined = models.DateTimeField(default=now, verbose_name='date joined')
    email = models.EmailField(max_length=255, unique=True, verbose_name='email')
    groups = models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')
    user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    class  Meta:
        verbose_name = 'user'

class Stores(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=150)
    identifier = models.CharField(max_length=30)
    brand = models.ForeignKey("supermarket.Brands", verbose_name=("brand"), on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

class Brands(models.Model):
    name = models.CharField(max_length=80)
    logo = models.CharField(max_length=255)


    
class Deals(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(name="price")
    image = models.CharField(max_length=255)
    store = models.ForeignKey("supermarket.Stores", verbose_name=("store"), on_delete=models.CASCADE)
    


