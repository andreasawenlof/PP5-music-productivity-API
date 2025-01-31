from django.contrib import admin
from .models import Album

# Register your models here.


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'created_at')
    list_filter = ('title', 'created_at')
    ordering = ('-created_at',)
