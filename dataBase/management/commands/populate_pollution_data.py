from django.core.management.base import BaseCommand
from dataBase.models import PollutionData
import pandas as pd

class Command(BaseCommand):
    help = 'Populate CountryData model'

    def handle(self, *args, **options):
        countryData = pd.read_csv('static\global air pollution dataset.csv')
        for index, row in countryData.iterrows():
            country = row['Country']
            city = row['City']
            aqi_value = row['AQI Value']
            aqi_category = row['AQI Category']
            co_aqi_category = row['CO AQI Category']
            co_aqi_value = row['CO AQI Value']
            ozone_aqi_value = row['Ozone AQI Value']
            ozone_aqi_category = row['Ozone AQI Category']
            no2_aqi_value = row['NO2 AQI Value']
            no2_aqi_category = row['NO2 AQI Category']
            pm25_aqi_value = row['PM2.5 AQI Value']
            pm25_aqi_category = row['PM2.5 AQI Category']
            
            pollution_data = PollutionData(
                country=country,
                city=city,
                aqi_value=aqi_value,
                aqi_category=aqi_category,
                co_aqi_value=co_aqi_value,
                co_aqi_category=co_aqi_category,
                ozone_aqi_value=ozone_aqi_value,
                ozone_aqi_category=ozone_aqi_category,
                no2_aqi_value=no2_aqi_value,
                no2_aqi_category=no2_aqi_category,
                pm25_aqi_value=pm25_aqi_value,
                pm25_aqi_category=pm25_aqi_category
            )
            
            pollution_data.save()