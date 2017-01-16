#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post

admin.site.register(Post) # Post class 를 관리자 페이지에서 볼수 있도록 모델 등록.

# Register your models here.
