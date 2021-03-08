from django.db import models
from django.db.models import Model


# class Insurance(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Issue(models.Model):
#     insurance = models.ForeignKey(Insurance)
#     fio = models.CharField(max_length=255)
#     iin = models.CharField(max_length=255)
#     price = models.TextField()
#
#     def __str__(self):
#         return self.name


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
