from django.db import models

class columns(models.Model):
    user_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    review = models.CharField(max_length=255)