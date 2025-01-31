from django.contrib import admin
from .models import Instrument, InstrumentCategory


class InstrumentInline(admin.TabularInline):
    model = Instrument
    extra = 1  # Allows adding instruments inside a category


@admin.register(InstrumentCategory)
class InstrumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [InstrumentInline]  # This puts instruments inside categories


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Shows category in instrument list
    search_fields = ('name',)
