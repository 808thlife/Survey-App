from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse

from accounts.models import User
from questions.models import Survey, Answer
from questions import utils

from .utils import validate_surveys

def index(request):
    current_user = request.user
    validation = validate_surveys(current_user)

    context = {}

    if validation == False:
        context = {"alert": True} # show alert
    else:
        print("False")
        context = {"alert": False}

    return render(request, "core/index.html", context)

def inbox(request):
    current_user = request.user
    surveys = Survey.objects.filter(~Q(is_answered__in=[request.user]))
    utils.validate_surveys()
    context = {"surveys":surveys }
    print(surveys)
    return render(request, "core/surveys.html", context)

def surveyView(request, ID):
    users = User.objects.all() # users stands for organisations
    survey = Survey.objects.get(id = ID)
    if request.user in survey.is_answered.all():
        return HttpResponseRedirect(reverse("core:inbox"))
    context = {"survey":survey, "users":users}
    return render(request, "core/survey.html", context)

def profileView(request, username):
    user = User.objects.get(username = username)
    surveys = Answer.objects.filter(user = user)
    context = {"user":user}
    return render(request, "core/pages-profile.html")

def loginView(request):
    return render(request, "core/authentication-login1.html")