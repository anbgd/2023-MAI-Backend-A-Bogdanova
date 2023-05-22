from app.models import Country, Breed
from django.contrib import admin


class Admin(admin.ModelAdmin):
    list_display = ("id", "breed_name")


class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Breed, Admin)
admin.site.register(Country, CountryAdmin)