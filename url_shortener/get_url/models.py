from django.db import models

# Create your models here.
class URLMapping(models.Model):
    original_url = models.URLField()
    short_url = models.URLField()
    mapping_string = models.CharField(max_length=6, unique=True)
