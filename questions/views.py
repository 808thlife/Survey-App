from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from questions.models import Survey

# Create your views here.
def submit_survey(request):
    if request.method == "POST":
        survey = request.POST["survey"]
        answer = request.POST["answer"]

        survey = Survey.objects.get(question = survey)
        print(survey.is_answered)
        survey.is_answered = True
        survey.save()
        
        return HttpResponseRedirect(reverse("core:inbox"))
        