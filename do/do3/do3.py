import redis
from do.do1.do1 import random_codes

codes = random_codes(4, 4, 100)
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

for c in codes:
    r.sadd('code', c)
