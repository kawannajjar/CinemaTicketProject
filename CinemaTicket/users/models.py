from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
import uuid

class Role(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    USER = 'User', 'User'

class UserManager(BaseUserManager):
    def create_user(self, email, birthdate, password=None, **extra_fields):
        if not email:
            raise ValueError('ایمیل الزامی است')
        user = self.model(
            email=self.normalize_email(email),
            birthdate=birthdate,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, birthdate, password=None, **extra_fields):
        extra_fields.setdefault('role', Role.ADMIN)
        return self.create_user(email, birthdate, password, **extra_fields)

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    registration_date = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=5, choices=Role.choices, default=Role.USER)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birthdate']
    
    objects = UserManager()