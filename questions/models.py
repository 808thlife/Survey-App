from django.db import models
from accounts.models import User

_ = lambda s: s # placeholder

class Survey(models.Model):
    question = models.CharField(max_length=50)
    answer = models.TextField()
    organisations = models.ManyToManyField(User, blank = True, related_name = "organisations")
    is_answered = models.BooleanField()
    all = models.BooleanField()
    expired = models.BooleanField() # to track the time
    timestamp = models.DateField(auto_now_add=True)
    frequency = models.IntegerField(default = 1)

    def __str__(self):
        return self.question
    
