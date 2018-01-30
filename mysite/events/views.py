# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def events(request):
    template="events.html"
    context = {

    }
    return render(request , template, context)
