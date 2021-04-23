from django.http import JsonResponse

from ZerodhaTask import REDIS


def fetch_all(request):
    results = []
    for key in REDIS.scan_iter("*"):
        field_dict = REDIS.hgetall(key)

        results.append({
            'code' : field_dict['SC_CODE'],
            'name' : key,
            'open' : field_dict['OPEN'],
            'high' : field_dict['HIGH'],
            'low'  : field_dict['LOW'],
            'close': field_dict['CLOSE']
        })

    return JsonResponse(
        results, safe=False
    )
