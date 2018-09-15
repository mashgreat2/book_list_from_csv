# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name