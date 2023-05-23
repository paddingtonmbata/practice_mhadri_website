from django.contrib import admin
from .models import CountryData, PollutionData
# Register your models here.

class CountryDataAdmin(admin.ModelAdmin):
    search_fields = ['country_name']

class PollutionDataAdmin(admin.ModelAdmin):
    search_fields = ['country', 'city']

admin.site.register(CountryData, CountryDataAdmin)
admin.site.register(PollutionData, PollutionDataAdmin)