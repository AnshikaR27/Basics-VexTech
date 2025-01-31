from django.contrib import admin
from .models import HomepageContent

class HomepageContentAdmin(admin.ModelAdmin):
    list_display = ('text', 'last_updated')

admin.site.register(HomepageContent, HomepageContentAdmin)