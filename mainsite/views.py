from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

from mainsite.models import News
# from mainsite.forms import FormCreate


def index(request):
    list = News.objects.all().order_by('-id')[:3]
    context = {"list": list}
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
    # upload = FormCreate()
    # if request.method == 'POST':
    #     upload = DeliveryCreate(request.POST, request.FILES)
    #     if upload.is_valid():
    #         upload.save()
    #         return redirect('/delivery')
    #     else:
    #         return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/delivery'}}">reload</a>""")
    # else:
    #     context = {
    #         "upload_form": upload,
    #         "action": "Добавить"
    #     }
    #     return render(request, 'delivery/create.html', context)
    context = {}
    context['segment'] = 'contact'

    html_template = loader.get_template('main-site/contact.html')
    return HttpResponse(html_template.render(context, request))


def news(request):
    list = News.objects.all()
    context = {"list": list}
    context['segment'] = 'news'

    html_template = loader.get_template('main-site/news.html')
    return HttpResponse(html_template.render(context, request))
