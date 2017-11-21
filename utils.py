import requests
import json
import redis
import os

from sutime import SUTime

def count_words_at_url(query, callback_url, callback_data, random_id):
  # from worker import sutime
  # jar_files = os.path.join(os.path.dirname(__file__), 'jars')
  # sutime = SUTime(jars=jar_files, mark_time_ranges=False)
  # from worker import sutime

  jar_files = os.path.join(os.path.dirname(__file__), 'jars')
  sutime = SUTime(jars=jar_files, mark_time_ranges=False)
  # print(sutime)
  redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
  print("query")
  print(query)
  print("callback_url")
  print(callback_url)
  print("callback_data")
  print(callback_data)
  sutime_result = sutime.parse(query)
  result = {}
  result["callback_data"] = callback_data
  result["sutime_result"] = sutime_result
  conn = redis.from_url(redis_url)
  conn.set(str(random_id), str(sutime_result))
  print("result set")
  cmd = "curl -X POST -H 'Content-Type: application/json' -d '{}' '{}' ".format(json.dumps(result), callback_url)
  print(cmd)
  os.popen(cmd).read()
  return {}