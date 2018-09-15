# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from publisher.models import Publisher
from django.views.generic import ListView

# Create your views here.
class PublisherList(ListView):
    model = Publisher
    template_name = 'publishers-list.html'