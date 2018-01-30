from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_model_list_view, name='post_list'),
]
