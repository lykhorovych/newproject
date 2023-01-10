from django.contrib import admin

from cities.models import City

# Register your models here.

admin.site.register(City)
admin.site.site_header = 'Мій проект'