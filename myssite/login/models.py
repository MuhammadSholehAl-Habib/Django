# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=40)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name
