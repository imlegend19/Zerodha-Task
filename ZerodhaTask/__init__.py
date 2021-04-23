import os
from urllib.parse import urlparse

import redis

redis_url = urlparse(os.environ.get("REDIS_URL"))

REDIS = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    username=redis_url.username,
    password=redis_url.password,
    ssl=True,
    ssl_cert_reqs=None
)
