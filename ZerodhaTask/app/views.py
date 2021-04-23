from django.http import JsonResponse

from ZerodhaTask import REDIS


def search(request, query):
    print(f"got query for {query}")
    results = []
    for key in REDIS.scan_iter(f"*{query.upper()}*"):
        field_dict = REDIS.hgetall(key)

        results.append({
            'code' : field_dict[b'code'].decode(),
            'name' : key.decode(),
            'open' : field_dict[b'open'].decode(),
            'high' : field_dict[b'high'].decode(),
            'low'  : field_dict[b'low'].decode(),
            'close': field_dict[b'close'].decode(),
        })

    print(f"found {len(results)}")

    return JsonResponse(
        results, safe=False
    )
