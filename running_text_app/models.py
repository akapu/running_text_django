from django.db import models

class Query(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=100)
