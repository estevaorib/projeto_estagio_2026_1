from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    job_title = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
