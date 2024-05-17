from django.db import models
from accounts.models import User
from django.utils import timezone


_ = lambda s: s # placeholder

class Survey(models.Model):
    question = models.CharField(max_length=50)
    organisations = models.ManyToManyField(User, blank = True, related_name = "organisations")
    is_answered = models.ManyToManyField(User, blank = True, related_name = "already_answered")
    expired = models.BooleanField(default = False) # to track the time
    timestamp = models.DateField(auto_now_add = True)
    frequency = models.IntegerField(default = 1)

    def __str__(self):
        return self.question

    
class Answer(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE, related_name = "get_survey")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.TextField(default = "Not Answered")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"answer from {self.user}"