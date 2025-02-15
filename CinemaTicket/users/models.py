from datetime import date 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, birthdate, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()  # تاریخ تولد
    registration_date = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=5, choices=Role.choices, default=Role.USER)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birthdate']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def age(self):
        """محاسبه سن کاربر بر اساس تاریخ تولد"""
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))