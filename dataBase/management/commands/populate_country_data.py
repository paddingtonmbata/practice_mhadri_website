from django.core.management.base import BaseCommand
from dataBase.models import CountryData

class Command(BaseCommand):
    help = 'Populate CountryData model'

    def handle(self, *args, **options):
        countryData = {
            "Afghanistan": 0,
            "Albania": 0,
            "Algeria": 0,
            "American Samoa": 0,
            "Andorra": 0,
            "Angola": 0,
            "Anguilla": 0,
            "Antarctica": 0,
            "Antigua and Barbuda": 0,
            "Argentina": 0,
            "Armenia": 0,
            "Aruba": 0,
            "Australia": 0,
            "Austria": 0,
            "Azerbaijan": 0,
            "Bahamas": 0,
            "Bahrain": 0,
            "Bangladesh": 0,
            "Barbados": 0,
            "Belarus": 0,
            "Belgium": 0,
            "Belize": 0,
            "Benin": 0,
            "Bermuda": 0,
            "Bhutan": 0,
            "Bolivia": 0,
            "Bosnia and Herzegovina": 0,
            "Botswana": 0,
            "Bouvet Island": 0,
            "Brazil": 0,
            "British Indian Ocean Territory": 0,
            "Brunei Darussalam": 0,
            "Bulgaria": 0,
            "Burkina Faso": 0,
            "Burundi": 0,
            "Cambodia": 0,
            "Cameroon": 0,
            "Canada": 4,
            "Cape Verde": 0,
            "Cayman Islands": 0,
            "Central African Rep.": 0,
            "Chad": 0,
            "Chile": 0,
            "China": 0,
            "Christmas Island": 0,
            "Cocos (Keeling) Islands": 0,
            "Colombia": 0,
            "Comoros": 0,
            "Congo": 0,
            "Dem. Rep. Congo": 0,
            "Cook Islands": 0,
            "Costa Rica": 0,
            "C\u00f4te d'Ivoire": 0,
            "Croatia": 0,
            "Cuba": 0,
            "Cyprus": 0,
            "N. Cyprus":0,
            "Czech Republic": 0,
            "Denmark": 1,
            "Djibouti": 0,
            "Dominica": 0,
            "Dominican Republic": 0,
            "Ecuador": 0,
            "Egypt": 0,
            "El Salvador": 0,
            "Equatorial Guinea": 0,
            "Eritrea": 0,
            "Estonia": 0,
            "Ethiopia": 0,
            "Falkland Islands (Malvinas)": 0,
            "Faroe Islands": 0,
            "Fiji": 0,
            "Finland": 0,
            "France": 0,
            "French Guiana": 0,
            "French Polynesia": 0,
            "Fr. S. Antarctic Lands": 0,
            "Gabon": 0,
            "Gambia": 0,
            "Georgia": 0,
            "Germany": 0,
            "Ghana": 0,
            "Gibraltar": 0,
            "Greece": 0,
            "Greenland": 0,
            "Grenada": 0,
            "Guadeloupe": 0,
            "Guam": 0,
            "Guatemala": 0,
            "Guernsey": 0,
            "Guinea": 0,
            "Guinea-Bissau": 0,
            "Guyana": 0,
            "Haiti": 0,
            "Heard Island and Mcdonald Islands": 0,
            "Holy See (Vatican City State)": 0,
            "Honduras": 0,
            "Hong Kong": 0,
            "Hungary": 0,
            "Iceland": 0,
            "India": 0,
            "Indonesia": 0,
            "Iran": 0,
            "Iraq": 0,
            "Ireland": 1,
            "Isle of Man": 0,
            "Israel": 0,
            "Italy": 0,
            "Jamaica": 0,
            "Japan": 0,
            "Jersey": 0,
            "Jordan": 0,
            "Kazakhstan": 0,
            "Kenya": 0,
            "Kiribati": 0,
            "Korea, Democratic People's Republic of": 0,
            "Korea, Republic of": 0,
            "Kosovo":0,
            "Kuwait": 0,
            "Kyrgyzstan": 0,
            "Laos": 0,
            "Latvia": 0,
            "Lebanon": 0,
            "Lesotho": 0,
            "Liberia": 0,
            "Libya": 0,
            "Liechtenstein": 0,
            "Lithuania": 0,
            "Luxembourg": 0,
            "Macao": 0,
            "Macedonia": 0,
            "Madagascar": 0,
            "Malawi": 0,
            "Malaysia": 0,
            "Maldives": 0,
            "Mali": 0,
            "Malta": 0,
            "Marshall Islands": 0,
            "Martinique": 0,
            "Mauritania": 0,
            "Mauritius": 0,
            "Mayotte": 0,
            "Mexico": 0,
            "Micronesia, Federated States of": 0,
            "Moldova, Republic of": 0,
            "Monaco": 0,
            "Mongolia": 0,
            "Montenegro": 0,
            "Montserrat": 0,
            "Morocco": 0,
            "Mozambique": 0,
            "Myanmar": 0,
            "Namibia": 0,
            "Nauru": 0,
            "Nepal": 0,
            "Netherlands": 0,
            "Netherlands Antilles": 0,
            "New Caledonia": 0,
            "New Zealand": 0,
            "Nicaragua": 0,
            "Niger": 0,
            "Nigeria": 0,
            "Niue": 0,
            "Norfolk Island": 0,
            "Northern Mariana Islands": 0,
            "Norway": 3,
            "Oman": 0,
            "Pakistan": 0,
            "Palau": 0,
            "Palestine": 0,
            "Panama": 0,
            "Papua New Guinea": 0,
            "Paraguay": 0,
            "Peru": 0,
            "Philippines": 0,
            "Pitcairn": 0,
            "Poland": 0,
            "Portugal": 0,
            "Puerto Rico": 0,
            "Qatar": 0,
            "Reunion": 0,
            "Romania": 0,
            "Russia": 0,
            "Rwanda": 0,
            "Saint Helena": 0,
            "Saint Kitts and Nevis": 0,
            "Saint Lucia": 0,
            "Saint Pierre and Miquelon": 0,
            "Saint Vincent and the Grenadines": 0,
            "Samoa": 0,
            "San Marino": 0,
            "Sao Tome and Principe": 0,
            "Saudi Arabia": 0,
            "Senegal": 0,
            "Serbia": 0,
            "Seychelles": 0,
            "Sierra Leone": 0,
            "Singapore": 0,
            "Slovakia": 0,
            "Slovenia": 0,
            "Solomon Islands": 0,
            "Somalia": 0,
            "Somaliland": 0,
            "South Africa": 1,
            "South Georgia and the South Sandwich Islands": 0,
            "South Sudan":0,
            "Spain": 0,
            "Sri Lanka": 0,
            "Sudan": 0,
            "Suriname": 0,
            "Svalbard and Jan Mayen": 0,
            "Swaziland": 0,
            "Sweden": 0,
            "Switzerland": 0,
            "Syria": 0,
            "Taiwan": 0,
            "Tajikistan": 0,
            "Tanzania": 0,
            "Thailand": 0,
            "Timor-leste": 0,
            "Togo": 0,
            "Tokelau": 0,
            "Tonga": 0,
            "Trinidad and Tobago": 0,
            "Tunisia": 0,
            "Turkey": 0,
            "Turkmenistan": 0,
            "Turks and Caicos Islands": 0,
            "Tuvalu": 0,
            "Uganda": 0,
            "Ukraine": 0,
            "United Arab Emirates": 0,
            "United Kingdom": 4,
            "United States": 8,
            "United States Minor Outlying Islands": 0,
            "Uruguay": 0,
            "Uzbekistan": 0,
            "Vanuatu": 0,
            "Venezuela": 0,
            "Vietnam": 0,
            "Virgin Islands, British": 0,
            "Virgin Islands, U.S.": 0,
            "Wallis and Futuna": 0,
            "W. Sahara": 0,
            "Yemen": 0,
            "Zambia": 0,
            "Zimbabwe": 0
        }


        for country, data_value in countryData.items():
            CountryData.objects.create(country_name=country, data_value=data_value)
