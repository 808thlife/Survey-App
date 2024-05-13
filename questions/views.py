from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from questions.models import Survey, Answer

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
        