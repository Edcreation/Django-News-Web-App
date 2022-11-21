from django.contrib import admin

from .models import Newsfeed

# Register your models here.

class NewsfeedAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Newsfeed, NewsfeedAdmin)