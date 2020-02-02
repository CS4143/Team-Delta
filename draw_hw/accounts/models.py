from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, is_student=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')
            
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            is_student = is_student
        )
        user.set_password(password)
        user.save()
        return user
      
    def create_superuser(self, email, username, is_student, password):
        user = self.create_user(
            email,
            username,
            is_student,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    is_student = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'is_student']
    
    def __str__(self):
        return "@{}".format(self.username)