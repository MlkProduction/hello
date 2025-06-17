from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    tags = ["Hexlet - Django - Blog"]
    return render(
        request,
        "articles/index.html",
        context={"tags": tags},
    )
