from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    web_site = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
