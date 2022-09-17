from django.contrib import admin
from .models import Category, Event, Venue

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Category, CategoryAdmin)

class VenueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Venue, VenueAdmin)

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Event, EventAdmin)
