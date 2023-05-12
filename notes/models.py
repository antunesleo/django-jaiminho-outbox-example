from datetime import datetime

from django.db import models
from django.utils import timezone


class Note(models.Model):
   id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=255)
   content = models.TextField()
   created_at = models.DateTimeField(default=timezone.now)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.title

   def as_dict(self):
       return {
           "id": self.id,
           "title": str(self.title),
           "content": str(self.content),
           "created_at": datetime.strftime(self.created_at, "%Y-%m-%d %H:%M:%S"),
           "updated_at": datetime.strftime(self.updated_at, "%Y-%m-%d %H:%M:%S"),
       }
