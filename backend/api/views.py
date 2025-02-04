from django.shortcuts import render
from django.http import JsonResponse

def quran_surahs(request):
    surahs = [
        {"id": 1, "name": "Al-Fatiha", "verses": 7},
        {"id": 2, "name": "Al-Baqarah", "verses": 286},
        {"id": 3, "name": "Al-Imran", "verses": 200},
    ]
    return JsonResponse(surahs, safe=False)

