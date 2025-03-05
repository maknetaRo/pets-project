from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

