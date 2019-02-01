# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rango.models import UserProfile

from django.contrib import admin
# Register your models here.
from rango.models import Category, Page
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url');
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
