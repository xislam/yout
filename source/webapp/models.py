from django.db import models


class URL(models.Model):
    link = models.URLField(blank=False)
    email = models.EmailField(max_length=255)