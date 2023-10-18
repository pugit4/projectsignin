from django.db import models

# Create your models here.
class govt_sign(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    documents = models.FileField(upload_to='upload/')
    photo = models.ImageField(upload_to='image/')
    