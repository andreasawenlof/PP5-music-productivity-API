from django.contrib import admin

# Register your models here.


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'assigned_user', 'created_at')
    list_filter = ('album', 'assigned_user', 'created_at')
    search_fields = ('title', 'album__title', 'assigned_user__username')
    ordering = ('-created_at',)


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'created_at')
    search_fields = ('title', 'artist')
    ordering = ('-created_at',)
