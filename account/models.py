from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _ # for translating later on


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_sactive', True)

        if not other_fields.get('is_staff'):
            raise ValueError(
                'Superuser\'s is_staff field must be set to True'
            )
        if not other_fields.get('is_superuser'):
            raise ValueError(
                'Superuser\'s is_superuser field must be set to True'
            )

        return self.create_user(email, user_name, password, **other_fields)
        
    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide and email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()

        return user

class UserBase(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    contact_number = PhoneNumberField(region='US')

    # user status, maybe we have some legal obligation to keep data
    # instead of straight up deleting
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'contact_number']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.user_name
    
