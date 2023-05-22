from django.core.handlers.asgi import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Country, Breed
from rest_framework import generics
from .serializers import CountrySerializer, BreedSerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


@csrf_exempt
@require_http_methods(["GET"])
def search(request: HttpRequest) -> JsonResponse:
    search_query = request.GET.get("query")
    breeds = Breed.objects.filter(title__icontains=search_query)
    data = [{"id": str(f.id), "breed_name": f.breed_name} for f in breeds]
    return JsonResponse({"data": data})


@csrf_exempt
@require_http_methods(["POST"])
def add_breed(request: HttpRequest) -> JsonResponse:
    breed_name = request.POST.get("breed_name")
    country_name = request.POST.get("country_name")

    country, created = Country.objects.get_or_create(name=country_name)

    breed = Breed.objects.create(breed_name=breed_name)
    breed.countries.add(country)
    breed.save()
    return JsonResponse({"id": str(breed.id)})


@csrf_exempt
@require_http_methods(["GET"])
def get_all(request: HttpRequest) -> JsonResponse:
    breeds = Breed.objects.all()
    data = [{"id": str(f.id), "breed_name": f.breed_name} for f in breeds]
    return JsonResponse({"data": data})


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "Boom.html")