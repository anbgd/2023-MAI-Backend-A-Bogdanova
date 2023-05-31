from django.contrib.auth.decorators import login_required
from django.core.handlers.asgi import HttpRequest, HttpResponse
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from rest_framework import generics



@csrf_exempt
@require_http_methods(["GET"])
def search(request: HttpRequest) -> JsonResponse:
    search_query = request.GET.get("query")
    data = [{"id": "23423", "title": "It", "year": "2017"}]
    return JsonResponse({"data": data})


@csrf_exempt
@require_http_methods(["POST"])
def add_film(request: HttpRequest) -> JsonResponse:
    title = request.POST.get("title")
    year = request.POST.get("year")
    # director_name = request.POST.get("director_name")
    return JsonResponse({"id": "2017"})


@csrf_exempt
@require_http_methods(["GET"])
def get_all(request: HttpRequest) -> JsonResponse:
    data = [{"id": '123345', "title": "Hell or High Water", "year": "2016"}]
    return JsonResponse({"data": data})


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "cat.html")
