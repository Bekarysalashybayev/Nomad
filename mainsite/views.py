from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.template import loader

from mainsite.forms import FormCreate, IssueCreate
from mainsite.models import News, Insurance, TypeCar, City, Hospital


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
    context = {'segment': 'about'}

    html_template = loader.get_template('main-site/about.html')
    return HttpResponse(html_template.render(context, request))


def resources(request, insurance_id: int):
    context = {"id": insurance_id, 'segment': 'resources'}

    html_template = loader.get_template('main-site/resource.html')
    return HttpResponse(html_template.render(context, request))


def contact(request):
    upload = FormCreate()
    if request.method == 'POST':
        upload = FormCreate(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('/%2Fcontact')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/%2Fcontact'}}">reload</a>""")
    else:
        context = {
            "upload_form": upload,
            "action": "Добавить"
        }
        return render(request, 'main-site/contact.html', context)


def news(request):
    list = News.objects.all()
    context = {"list": list}
    context['segment'] = 'news'

    html_template = loader.get_template('main-site/news.html')
    return HttpResponse(html_template.render(context, request))


def news_detail(request, news_id: int):
    list = News.objects.get(pk=news_id)
    context = {"name": list.name, "img": list.img, "desc": list.description, "created_at": list.created_at}

    html_template = loader.get_template('main-site/news-detail.html')
    return HttpResponse(html_template.render(context, request))


def add_issue(request, insurance_id: int):
    upload = IssueCreate()
    if request.method == 'POST':
        upload = IssueCreate(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('/%2Fresources/'+insurance_id.__str__())
        else:
            return HttpResponse(
                """your form is wrong, reload on <a href = "{{ url : '/'}}">reload</a>""")

    insurance = Insurance.objects.get(pk=insurance_id)
    # type_car = TypeCar.objects.all()
    # hospital = Hospital.objects.all()
    cities = City.objects.all()
    list = {}
    title = ""
    title1 = ""
    if insurance_id == 2:
        title = "Страхование автомобиля"
        title1 = "Автомобиль"
        list = TypeCar.objects.all()
    elif insurance_id == 1:
        title = "Страхование здаровье"
        title1 = "Здаровье"
        list = Hospital.objects.all()
    elif insurance_id == 3:
        title = "Страхование путешествий"
        title1 = "Путешествие"
    elif insurance_id == 4:
        title = "Страхование имущества"
        title1 = "Имущество"

    context = {'insurance': insurance, 'list': list, 'city': cities, 'title': title, 'title1': title1}

    html_template = loader.get_template('main-site/add-issue.html')
    return HttpResponse(html_template.render(context, request))
