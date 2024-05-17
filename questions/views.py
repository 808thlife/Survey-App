from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from questions.models import Survey, Answer
from accounts.models import User

# Create your views here.
def submit_survey(request):
    if request.method == "POST":
        current_user = request.user
        survey = request.POST["survey"]
        answer = request.POST["answer"]

        survey = Survey.objects.get(question = survey)
        
        f = Answer(survey = survey, user = request.user)
        f.save()

        print(survey.is_answered)
        survey.is_answered.add(current_user)
        survey.save()
        
        return HttpResponseRedirect(reverse("core:inbox"))
        
def create_survey(request, ID): # function for a form on user's profile. id specifies user
    if request.method == "POST":
        user = User.objects.get(id = ID)
        print(user)
        survey_question = request.POST["survey"]

        f = Survey(question = survey_question)
        f.save()

        f.organisations.add(user)

        return HttpResponseRedirect(reverse("core:inbox"))