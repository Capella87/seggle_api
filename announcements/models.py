from django.conf import settings
from django.db import models
import rest_framework
from account.models import SeggleUser
# Create your models here.

class Announcement(models.Model):
    writer = models.ForeignKey(SeggleUser, on_delete=models.CASCADE, to_field="username")
    title = models.TextField(null=False, default='')
    description = models.TextField()
    created_time = models.DateTimeField(null=False, auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(null=False, auto_now=True)
    is_important = models.BooleanField(null=False, default=False)
    is_visible = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'announcement'