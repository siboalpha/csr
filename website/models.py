from django.db import models

# Create your models here.
class contactMessage(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name