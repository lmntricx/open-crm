# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users

# Create your views here.


def login(request):
    users = Users.objects.all().values()

    template = loader.get_template('index.html')
    context = {
        'Users': users,
    }

    return HttpResponse(template.render(context, request))

