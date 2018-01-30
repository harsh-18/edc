# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import PostModel

def post_model_detail_view(request):
    return render(request , template_path, context)

def post_model_list_view(request):
    qs = PostModel.objects.all()
    template_path="blog/list_view.html"
    context = {
    "object_list": qs
    }
    return render(request , template_path , context)
