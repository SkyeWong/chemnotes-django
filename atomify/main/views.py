from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout


def index(request):
    template = loader.get_template("main/index.html")
    return HttpResponse(template.render(request=request))


def logout_view(request):
    logout(request)
    return redirect("/")
