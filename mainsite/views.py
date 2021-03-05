from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader


def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('main-site/index.html')
    return HttpResponse(html_template.render(context, request))


def insurance(request):
    context = {}
    context['segment'] = 'insurance'

    html_template = loader.get_template('main-site/insurance.html')
    return HttpResponse(html_template.render(context, request))


def about(request):
    context = {}
    context['segment'] = 'about'

    html_template = loader.get_template('main-site/about.html')
    return HttpResponse(html_template.render(context, request))


def resources(request):
    context = {}
    context['segment'] = 'resources'

    html_template = loader.get_template('main-site/resource.html')
    return HttpResponse(html_template.render(context, request))


def contact(request):
    context = {}
    context['segment'] = 'contact'

    html_template = loader.get_template('main-site/contact.html')
    return HttpResponse(html_template.render(context, request))