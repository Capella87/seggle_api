from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

'''
username
name
(password)
email
'''

class SeggleUserManager(BaseUserManager):

    def create_user(self, username, email, name, password=None):
        if not username:
            raise ValueError('Please specify username.')
        if not email:
            raise ValueError('Please specify valid email.')
        if not password:
            raise ValueError('Please specify password.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, username, email, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            name=name
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class SeggleUser(AbstractBaseUser, PermissionsMixin):

    # Fields
    username = models.CharField(max_length=30, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=50, null=False)

    joined_date = models.DateTimeField(auto_now_add=True)

    #PermissionsMixin models
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) #계정 활성 여부
    is_staff = models.BooleanField(default=False) #True: admin 화면 로그인
    is_admin = models.BooleanField(default=False)

    #AbstractBaseUser models

    #AbstractBaseUser things
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'name']

    objects = SeggleUserManager() #상속

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user"


