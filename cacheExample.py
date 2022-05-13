import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'cacheExample'
from django.core.cache import cache
cache.set('my_key', 'hello, world!', 30)
cache.get('my_key')
cache.get('my_key', 'has expired')
'add will not attempt to update if key specified is already exist'
cache.set('add_key', 'Initial value')
cache.add('add_key', 'New value')
cache.get('add_key')
'get_many returns dict with key value pair and it will hits the cache once'
cache.set('a', 1)
cache.set('b', 2)
cache.set('c', 3)
cache.get_many(['a', 'b', 'c'])
'incremnetal data which already exists'
cache.set('num', 1)
cache.incr('num')
'result be like 2'
cache.incr('num', 10)
'result be like 12'
cache.decr('num')
cache.decr('num', 5)

'Set version 2 of a cache key'
cache.set('my_key', 'hello world!', version=2)
'Get the default version (assuming version=1) which is not available'
cache.get('my_key')
'Get version 2 of the same key'
cache.get('my_key', version=2)

'Increment the version of 'my_key' i.e. version=3'
cache.incr_version('my_key')
cache.get('my_key')
cache.get('my_key', version=2)
cache.get('my_key', version=3)
