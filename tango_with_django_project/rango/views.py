# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rango.models import Category
from rango.models import Page
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def show_category(request, category_name_slug):
# Create a context dictionary which we can pass # to the template rendering engine. context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
# We get here if we didn't find the specified category. # Don't do anything -
 # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
# Note the key boldmessage is the same as {{ boldmessage }} in the template!
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)
