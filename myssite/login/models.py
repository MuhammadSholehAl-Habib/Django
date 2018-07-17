# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=40)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class marker(models.Model):
    name = models.CharField(max_length=40)
    lat = models.CharField(max_length=40)
    lng = models.CharField(max_length=40)
    address = models.TextField()

    def __str__(self):
        return self.name

class siapsat(models.Model):
    satuan = models.CharField(max_length=100)
    posisi = models.CharField(max_length=200)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    kotama = models.CharField(max_length=100)

    def __str__(self):
        return self.satuan

class organization(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()

    def __str__(self):
        return self.name

class ekko(models.Model):
    mantap = models.DecimalField(max_digits=5, decimal_places=2)
    satuan_id = models.IntegerField()

    def __str__(self):
        return self.satuan_id
