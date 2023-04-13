from django.db import models

# Create your models here.
from core.abstract.models import AbstractModel,AbstractManager

class PostManager(AbstractManager):
  pass

class Post(AbstractManager):
  author = models.ForeignKey(to="core_user.User",on_delete=models.CASCADE)
  
  body = models.TextField()
  
  edited = models.BooleanField(default=False)
  
  objects = PostManager()
  
  def __str__(self):
    return f"{self.author.name}"
  
  
  class Meta:
    db_table = "'core.post'"