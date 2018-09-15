# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from author.models import Author
from publisher.models import Publisher

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    isbn = models.BigIntegerField(default=0, null=True)
    isbn_13 = models.BigIntegerField(default=0, null=True)
    authors = models.ManyToManyField(Author, blank=True)
    # publisher = models.ForeignKey(Publisher, null=True)
    publication_date = models.IntegerField(null=True, default=-1)
    ratings_count = models.BigIntegerField(default=0, null=True)
    average_ratings = models.DecimalField(max_digits=20, decimal_places=2, null=True, )
    cover_image_url = models.URLField(null=True)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
