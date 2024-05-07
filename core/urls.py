from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name = "index"),
    path("inbox", views.inbox, name = "inbox"),
    path("inbox/<int:ID>", views.surveyView, name = "surveyView")
]
