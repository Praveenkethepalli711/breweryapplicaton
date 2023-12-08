from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Brewery(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    name = models.CharField(max_length=255)
    brewery_type = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=255)
    phone = models.CharField(unique=True, max_length=10)

    def __str__(self):
        return self.name

class Rating(models.Model):
    brewery_phone = models.CharField(max_length=10, primary_key=True, default=0)
    stars = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, related_name='ratings', to_field='phone')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line

    def __str__(self):
        return f"{self.brewery.name} - {self.stars} stars"