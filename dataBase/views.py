from django.shortcuts import render
from django.http import JsonResponse
from .models import CountryData
# Create your views here.
def index(request):
    return render(request, 'index.html')

def country_data_json(request):
    country_data = CountryData.objects.all().values('country_name', 'data_value')
    return JsonResponse(list(country_data), safe=False)