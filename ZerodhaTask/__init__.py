from urllib.parse import urlparse

import redis

redis_url = urlparse(
    'redis://:p97b4319d2a1b9515a467c740ba02fd0d23923a3cece162a1238b46bcba354350@ec2-18-215-213-65.compute-1.amazonaws'
    '.com:32570 '
)

REDIS = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    username=redis_url.username,
    password=redis_url.password,
    ssl=True,
    ssl_cert_reqs=None
)
