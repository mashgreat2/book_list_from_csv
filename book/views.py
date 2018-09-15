# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView

from book.models import Book
# Create your views here.


class BookList(ListView):
    model = Book
    template_name = 'book-list.html'

    def get_queryset(self):
        queryset = Book.objects.get_queryset().order_by('-average_ratings')
        # return super(BookList, self).get_queryset()
        return queryset[:300]

