from django.db import models

from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password, first_name, last_name,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError(_('Email is required'))
        email = self.normalize_email(email)
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          is_staff=is_staff, is_active=False,
                          is_superuser=is_superuser, last_login=now, date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        return self._create_user(email, password, first_name, last_name, is_staff=False,
                                 is_superuser=False, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        user = self._create_user(email, password, first_name, last_name, is_staff=True,
                                 is_superuser=True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), max_length=100, unique=True,
                              help_text=_('Required. 100 characters or fewer. '
                                          'Letters, numbers and @/./+/-/_ characters'))
    first_name = models.CharField(_('first name'), max_length=30, blank=False, null=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=False, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('user')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
