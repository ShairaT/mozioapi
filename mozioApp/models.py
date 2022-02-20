from django.db import models
from phone_field import PhoneField

LANGUAGE_CHOICES = [
    ('ENG', 'English'),
    ('SPA', 'Spanish'),
    ('CHI', 'Chinese'),
    ('FRA', 'French'),
    ('GER', 'German'),
    ('JPN', 'Japanese'),
]

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('JPY', 'Japanese Yen'),
    ('CNY', 'Chinese Yuan'),
    ('EUR', 'Euro'),
    ('GBP', 'Pound'),
    ('BTC', 'Bitcoin'),
    ('ETH', 'Ethereum'),
]

class Provider(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    language = models.CharField(max_length = 3, choices = LANGUAGE_CHOICES)
    currency = models.CharField(max_length = 3, choices = CURRENCY_CHOICES)

    def __str__(self):
        return self.name



class ServiceArea(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    name = models.CharField(max_length = 256, default = 'newpoly')
    price = models.DecimalField(max_digits = 6 , decimal_places = 2, default = 0.00 )
    polygon = models.TextField()

    def __str__(self):
        return self.name