from django.db import models


class CountryData(models.Model):
    country_name = models.CharField(max_length=100)
    data_value = models.IntegerField()

    def __str__(self):
        return self.country_name
