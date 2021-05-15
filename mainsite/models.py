from django.db import models
from django.db.models import Model


class Insurance(models.Model):
    name = models.CharField(max_length=255)
    doc1 = models.CharField(max_length=255, null=True)
    doc2 = models.CharField(max_length=255, null=True)
    doc3 = models.CharField(max_length=255, null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Issue(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.DO_NOTHING)
    fio = models.CharField(max_length=255)
    iin = models.CharField(max_length=255)
    bday = models.DateTimeField(null=True)
    doc1 = models.CharField(max_length=255, null=True)
    doc2 = models.CharField(max_length=255, null=True)
    doc3 = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.fio


class TypeCar(models.Model):
    name = models.CharField(max_length=15)


class City(models.Model):
    city = models.CharField(max_length=15)


class Hospital(models.Model):
    name = models.CharField(max_length=15)


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
