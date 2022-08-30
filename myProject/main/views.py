from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    template = "main/index.html"
    return render(request, template)


@login_required(login_url="/members/sign_in/?status=2")
def authenticated_view(request):
    template = "main/authenticated_view.html"
    return render(request, template)
