from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country_data_json/', views.country_data_json, name="country_data_json")
]
