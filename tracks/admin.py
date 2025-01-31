from django.contrib import admin
from .models import Track, Instrument

# Register your models here.


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'assigned_user', 'created_at')
    list_filter = ('album', 'assigned_user', 'created_at')
    search_fields = ('title', 'album__title', 'assigned_user__username')
    ordering = ('-created_at',)


admin.site.register(Instrument)
