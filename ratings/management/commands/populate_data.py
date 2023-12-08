import requests
from django.core.management.base import BaseCommand
from ratings.models import Brewery
import random
import string

class Command(BaseCommand):
    help = 'Populate data from API to the database'

    def handle(self, *args, **kwargs):
        api_url = 'https://api.openbrewerydb.org/v1/breweries'
        response = requests.get(api_url)
        breweries = response.json()

        for brewery_data in breweries:
            # Check if 'phone' key is available in brewery_data
            if 'phone' in brewery_data:
                phone = brewery_data['phone']
            else:
                # If 'phone' is not available, generate a random phone number
                phone = ''.join(random.choices(string.digits, k=10))

            Brewery.objects.create(phone=phone, name=brewery_data['name'])
