from django.core.cache import cache
from django.http import JsonResponse


def fetch_all(request):
    objects = cache.get_many(cache.keys("*"))

    return JsonResponse(
        list(dict(objects).values()),
        safe=False
    )
