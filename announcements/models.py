from django.conf import settings
from django.db import models
import rest_framework
# Create your models here.

class Announcement(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    title = models.TextField(null=False, default='')
    description = models.TextField()
    created_time = models.DateTimeField(null=False, auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(null=False, auto_now_add=True, auto_now=False)
    is_important = models.BooleanField(null=False, default=False)
    is_visible = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.id
