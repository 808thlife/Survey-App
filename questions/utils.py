from .models import Survey
from datetime import date, timedelta

def validate_surveys():
    processed_surveys = set()
    today = date.today()

    for survey in Survey.objects.filter(expired=False):
        expected_due_date = survey.timestamp + timedelta(days=survey.frequency)
        print(f"Expected due date for survey '{survey.question}' with timestamp {survey.timestamp} is {expected_due_date}")

        if expected_due_date <= today and survey not in processed_surveys:
            survey.expired = True
            survey.save()

            # Check for existing surveys with the same question and same timestamp
            existing_survey = Survey.objects.filter(question=survey.question, timestamp=today).first()
            if not existing_survey:
                new_survey = Survey.objects.create(
                    question=f"{survey.question} from {today}",
                    timestamp=today,
                    expired=False,
                    frequency=survey.frequency
                )

                # Adding organisations to the new survey
                new_survey.organisations.set(survey.organisations.all())

                print(f"New survey '{new_survey.question}' created (due today)!")
            else:
                print(f"Survey '{existing_survey.question}' already exists for today.")
            processed_surveys.add(survey)

        elif expected_due_date <= today:
            print(f"Survey '{survey.question}' has already been processed.")

    # Output a message if no surveys meet the conditions for processing
    if not Survey.objects.filter(expired=False, timestamp__lte=today).exists():
        print("No surveys require validation at this time.")
