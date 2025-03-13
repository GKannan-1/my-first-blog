from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# Create your views here.


def post_list(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/post_list.html", {})
