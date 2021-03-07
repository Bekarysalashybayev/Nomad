from django.contrib import admin

# Register your models here.
from mainsite.models import *

admin.site.register([News, ContactForm])