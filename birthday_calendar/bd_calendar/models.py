from django.db import models

# Create your models here.
class important_date(models.Model):
    date = models.DateField(required=True)