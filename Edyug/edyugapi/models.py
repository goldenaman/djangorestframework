from django.db import models

class People(models.Model):
    fname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)

