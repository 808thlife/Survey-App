from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("core:index"))
        
        else:
            return HttpResponseRedirect(reverse("core:loginView", kwargs = {"message": "Invalid username and/or password."}))
            # return render(request, "accounts/pages-login.html", {
            #     "message": "Invalid username and/or password."
            # })
    else:
        HttpResponseRedirect(reverse("core:inbox"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("core:loginView"))