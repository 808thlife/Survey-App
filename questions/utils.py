from .models import Survey
from datetime import date, timedelta

def validate_surveys():
    processed_surveys = set()
    today = date.today()
    #sdf
    #expected_due_date = survey.timestamp + timedelta(days=survey.frequency)

    for survey in Survey.objects.filter(expired = False):
        expected_due_date = survey.timestamp + timedelta(days=survey.frequency) # gets expected due date
        if expected_due_date >= today:

            check_surveys = Survey.objects.filter(question = f"{survey.question} on {expected_due_date}")
            if len(check_surveys) == 0:
                new_survey = survey
                new_survey.question = f"{survey.question} on {expected_due_date}"
                new_survey.pk = None
                new_survey.timestamp = expected_due_date
                new_survey.save()

                survey.expired = True
                survey.save()
                print("New survey was successfully created!")