from django.db import from django.db import models
import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class AbstractManager(models.Manager):
  
  def get_object_by_public_id(self, public_id):
    
    try:
      instance = self.get(public_id=public_id)
      return instance
    except (ObjectDoesNotExist, ValueError, TypeError):
      return Http404 