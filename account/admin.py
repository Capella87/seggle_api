from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.SeggleUser)
class SeggleUserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'email',
        'name',
        'joined_date',
        'is_superuser',
        'is_staff',
        'is_admin',
    )

    list_display_links = (
        'username',
        'email',
    )