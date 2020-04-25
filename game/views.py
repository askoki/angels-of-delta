import json
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from .consumers import default_key


def room(request):
    room_key = get_random_string(length=4).lower()
    cache.set(room_key, default_key)
    return JsonResponse({'room_key': room_key})