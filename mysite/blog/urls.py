from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_model_list_view, name='list'),
    url(r'^(?P<id>\d+)/$', views.post_model_detail_view, name='detail'),
]
