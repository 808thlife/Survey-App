from questions.models import Survey, Answer

def validate_surveys(current_user):
    all_surveys = Survey.objects.all()
    answered_surveys = current_user.already_answered.count()
    return answered_surveys == all_surveys.count()