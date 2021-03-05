from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader


def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('main-site/index.html')
    return HttpResponse(html_template.render(context, request))