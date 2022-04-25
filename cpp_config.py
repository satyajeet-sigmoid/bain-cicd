from redis import Redis
import os
# Configure Redis for storing the session data on the server-side
import redis
# SESSION_TYPE = 'redis'
# SESSION_PERMANENT = False
# SESSION_USE_SIGNER = True

SESSION_TYPE='redis'
SESSION_REDIS = redis.from_url('redis://localhost:6379')
# REDIS_URL = os.environ.get('REDIS_URL')
# SESSION_REDIS = redis.Redis.from_url(REDIS_URL)
# REDIS_URL = os.environ.get('REDIS_URL')

