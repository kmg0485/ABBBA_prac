from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, nickname, email, phonenumber, password=None, ):
        if not nickname:
            raise ValueError('Users must have a nickname')

        user = self.model(
            nickname=self.normalize_email(nickname),
            email = email,
            phonenumber=phonenumber
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, password=None):
        user = self.create_user(nickname, password=password,)
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    nickname = models.CharField(max_length=20, verbose_name='nickname', unique=True, blank=False)
    phonenumber = models.TextField(verbose_name='phonenumber',blank=True)
    email = models.EmailField(verbose_name='email', max_length=255, blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name="followers", blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin