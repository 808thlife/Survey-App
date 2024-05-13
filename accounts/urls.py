from django.urls import path

from . import  views

app_name = "accounts"

urlpatterns = [
    path("login/submit", views.login_view, name = "loginSubmit"),
    path("logout/", views.logout_view, name = "logout")
]
