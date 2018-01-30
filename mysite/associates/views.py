# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def associates(request):
    template="associates.html"
    context = {

    }
    return render(request , template, context)
