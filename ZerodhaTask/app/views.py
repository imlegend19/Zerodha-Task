from django.http import JsonResponse

from ZerodhaTask import REDIS


def get_results(s):
    results = []
    for key in REDIS.scan_iter(s):
        field_dict = REDIS.hgetall(key)

        results.append({
            'code' : field_dict[b'code'].decode(),
            'name' : key.decode(),
            'open' : field_dict[b'open'].decode(),
            'high' : field_dict[b'high'].decode(),
            'low'  : field_dict[b'low'].decode(),
            'close': field_dict[b'close'].decode(),
        })

    return results


def search(request, query):
    return JsonResponse(
        get_results(f"*{query.upper()}*"),
        safe=False
    )


def fetch_all(request):
    return JsonResponse(
        get_results('*'),
        safe=False
    )
