from django.db import models


class CountryData(models.Model):
    country_name = models.CharField(max_length=100)
    data_value = models.IntegerField()

    def __str__(self):
        return self.country_name


class PollutionData(models.Model):
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    aqi_value = models.IntegerField(null=True)
    aqi_category = models.CharField(max_length=100,null=True)
    co_aqi_value = models.IntegerField(null=True)
    co_aqi_category = models.CharField(max_length=100,null=True)
    ozone_aqi_value = models.IntegerField(null=True)
    ozone_aqi_category = models.CharField(max_length=100,null=True)
    no2_aqi_value = models.IntegerField(null=True)
    no2_aqi_category = models.CharField(max_length=100,null=True)
    pm25_aqi_value = models.IntegerField(null=True)
    pm25_aqi_category = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"AQI for {self.city}, {self.country}"