# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # ^:start, post/: URL should be include some keywork "post"
    # (?P<pk>[0-9]+) : everything that you input will pass to view using pk variable
    #                 /post/123334/ 형태로 숫자 0-9중에 입력이 가능하고 +는 하나 이상의 숫자가 필요
    # $ : it means last keyword
]
