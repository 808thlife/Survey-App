from django.shortcuts import render

from accounts.models import User
from questions.models import Survey

from .utils import validate_surveys

def index(request):
    return render(request, "core/index.html")

def inbox(request):
    current_user = request.user
    surveys = current_user.organisations.all().filter(is_answered = False).only("question", "id")
    
    context = {"surveys":surveys }
    print(surveys)
    return render(request, "core/surveys.html", context)

def surveyView(request, ID):
    users = User.objects.all() # users stands for organisations
    survey = Survey.objects.get(id = ID)
    context = {"survey":survey, "users":users}
    return render(request, "core/survey.html", context)