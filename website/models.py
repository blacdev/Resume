from django.db import models

class contact(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    subject = models.CharField(max_length = 80)
    message = models.TextField()
