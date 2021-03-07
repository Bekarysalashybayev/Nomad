from django.db import models
from django.db.models import Model


# class Delivery(models.Model):
#     fio = models.CharField(max_length=255)
#     img = models.ImageField(upload_to='images/', blank=True, null=True)
#     experience = models.CharField(max_length=255)
#     description = models.CharField(max_length=500)
#
#     def __str__(self):
#         return self.fio


class News(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
