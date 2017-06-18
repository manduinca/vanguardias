# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.core import validators
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from timezone_field import TimeZoneField

from apps.myuser import constants as myuser_constants


class MyUserManager(BaseUserManager):

    def create_user(self, username, email, password, first_name = '',
                    last_name = '', gender = 'O', *args, **kwargs):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            gender = gender,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_admin(self, username, email, password):
        user = self.create_user(
            username = username,
            email = email,
            password = password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using = self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        max_length = 20,
        unique = True,
        validators = [
            validators.RegexValidator(
                regex = r'^[a-zA-Z0-9-]{6,}$',
                message = _('Username must be Alphanumeric and have how minimum six characters'),
                code = 'invalid_username',
            ),
        ]
    )
    email = models.EmailField(
        max_length = 50,
        unique = True,
        validators = [validators.validate_email]
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER = (
        (MALE, _('male')),
        (FEMALE, _('female')),
        (OTHER, _('other')),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default=OTHER,
    )
    bio = models.TextField(
        blank=True,
        null=True,
    )
    occupation = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    workplace = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    website = models.URLField(
        max_length=150,
        blank=True,
        null=True,
    )
    birthday = models.DateField(
        blank=True,
        null=True,
    )
    country = models.ForeignKey(
        'cities_light.Country',
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    user_timezone = TimeZoneField(
        blank=True,
        null=True,
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
    )
    is_public = models.BooleanField(default=True)
    is_writer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    type = models.IntegerField(
        choices=myuser_constants.USER_TYPE,
        default=myuser_constants.MEMBER_TYPE
    )
    is_organization = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_absolute_url(self):
        return reverse(
            'user-profile',
            kwargs = {
                'username': self.username,
            },
        )

    @property
    def is_contact_info(self):
        backends = load_backends(settings.AUTHENTICATION_BACKENDS)
        for backend in backends:
            if len(self.social_auth.filter(provider = backend)):
                return True
        return False

    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'occupation': self.occupation,
            'bio': self.bio,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.get_full_name(),
            'url': self.get_absolute_url(),
            'is_writer': self.is_writer,
        }

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.username

    def get_full_name_or_short_name(self):
        return self.get_full_name() if self.get_full_name() \
            else self.get_short_name()

    def __unicode__(self):
        return self.username

    @property
    def get_object_name(self):
        return self.get_short_name()

    class Meta:
        db_table = 'myuser'
        verbose_name = _('user')
        verbose_name_plural = _('users')
