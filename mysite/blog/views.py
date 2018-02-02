# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import PostModel

def post_model_detail_view(request, id=None):
    obj = PostModel.objects.get(id=id)
    template="blog/detail_view.html"
    context = {
    "object": obj,
    }
    return render(request , template, context)

def post_model_list_view(request):
    qs = PostModel.objects.all() #query set
    recent_post = PostModel.objects.all().order_by('-timestamp')
    page = request.GET.get('page' , 1)
    paginator = Paginator(qs, 2)
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    template_path="blog/list_view.html"
    context = {
    "object_list": qs,
    "recent_post_list" : recent_post
    }
    return render(request , template_path , context)


# def recent_post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     # sorted the posts according to published_date
#     return render(request, 'blog/list_view.html', {'posts': posts})
    # render the blog posts with the page request
