# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def about_us(request):
    template="about_us/about-us.html"
    context = {

    }
    return render(request , template, context)
