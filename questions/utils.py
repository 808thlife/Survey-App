from .models import Survey
from datetime import date, timedelta

def validate_surveys():
    """
    Validates surveys, so it would create a new copy of X survey, when X is expired.
    X expired means that it passed expected_due_date. 
    """
    processed_surveys = set()
    today = date.today()

    for survey in Survey.objects.filter(expired = False):
        expected_due_date = survey.timestamp + timedelta(days=survey.frequency) # gets expected due date
        if expected_due_date <= today:

            check_surveys = Survey.objects.filter(question = f"{survey.question} on {expected_due_date}")
            if len(check_surveys) == 0:
                new_survey = survey
                new_survey.question = f"{survey.question} on {expected_due_date}"
                new_survey.pk = None
                new_survey.timestamp = expected_due_date
                new_survey.save()

                survey.expired = True # set expired to true in order to prevent dublicates.
                survey.save()
                print("New survey was successfully created!")