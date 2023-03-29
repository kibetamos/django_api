from django.db import models

# Create your models here.
import uuid

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class User(AbstractBaseUser, PermissionsMixin):
  public_id = models.UUIDField(db_index=True, unique=True,default=uuid.uuid4, editable=False)
  username = models.CharField(db_index=True,max_length=255, unique=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)