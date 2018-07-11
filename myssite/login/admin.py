# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Login, marker, siapsat, organization, ekko
# Register your models here.

admin.site.register(Login)
admin.site.register(marker)
admin.site.register(siapsat)
admin.site.register(organization)
admin.site.register(ekko)
