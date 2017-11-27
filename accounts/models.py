# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
# Abstractuser is what we target to override djangos default user system
from django.db import models
from django.utils import timezone
# Create your models here.

class AccountUserManager(UserManager):
	def m_create_user(self, username, email, password,
		is_staff, is_superuser, **extra_fields):
	# function creates a User with the given attributes (email/name/ect)
		now = timezone.now()
		if not email:
			raise ValueError('The given username must be set')

		email = self.normalize_email(email)
		user = self.model(username=email, email=email,
			is_superuser=is_superuser, is_staff=is_staff, 
			is_active=True, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self.db)

		return user

class User(AbstractUser):
    # now that we've abstracted this class we can add any
    # number of custom attribute to our user class
 
    # in later units we'll be adding things like payment details!
 
    objects = AccountUserManager()
				