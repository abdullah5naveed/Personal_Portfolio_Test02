from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    upload_date = models.DateTimeField()
    image = models.ImageField(blank=True, null=True, upload_to='blog/images')
    description = models.TextField()