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
    priority_type = models.CharField(max_length=20)
    combat_type = models.CharField(max_length=20)
    is_induk = models.BooleanField()
    is_rahwan = models.BooleanField()
    parent_id = models.IntegerField()
    level_0_id = models.IntegerField()
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    img_path = models.CharField(max_length=100)
    leader = models.CharField(max_length=50)
    vice_leader = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ekko(models.Model):
    personnel_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    personnel_quality = models.DecimalField(max_digits=5, decimal_places=2)
    personnel_mantap = models.DecimalField(max_digits=5, decimal_places=2)
    personnel_status = models.CharField(max_length=20)
    materiil_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    materiil_quality = models.DecimalField(max_digits=5, decimal_places=2)
    materiil_mantap = models.DecimalField(max_digits=5, decimal_places=2)
    materiil_status = models.CharField(max_length=20)
    exercise_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    exercise_quality = models.DecimalField(max_digits=5, decimal_places=2)
    exercise_mantap = models.DecimalField(max_digits=5, decimal_places=2)
    exercise_status = models.CharField(max_length=20)
    pangkalan_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    pangkalan_quality = models.DecimalField(max_digits=5, decimal_places=2)
    pangkalan_mantap = models.DecimalField(max_digits=5, decimal_places=2)
    pangkalan_status = models.CharField(max_length=20)
    penak_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    penak_quality = models.DecimalField(max_digits=5, decimal_places=2)
    penak_mantap = models.DecimalField(max_digits=5, decimal_places=2)
    penak_status = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    quality = models.DecimalField(max_digits=5, decimal_places=2)
    mantap = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20)
    induk = models.CharField(max_length=100)
    periode = models.CharField(max_length=20)
    year = models.IntegerField()
    satuan_id = models.IntegerField()

    def __str__(self):
        return self.satuan_id
