import os

import redis
from rq import Worker, Queue, Connection


listen = ['high', 'default', 'low']
import json
# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

# conn = redis.from_url(redis_url)
import os
from sutime import SUTime
from app import conn
if __name__ == '__main__':
  jar_files = os.path.join(os.path.dirname(__file__), 'jars')
  sutime = SUTime(jars=jar_files, mark_time_ranges=False)
  with Connection(conn):
    worker = Worker(map(Queue, listen))
    while True:
      job = worker.dequeue_job_and_maintain_ttl(420)[0]
      args = job.args
      query = args[0]
      callback_url = args[1]
      callback_data = args[2]
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
      cmd = "curl -X POST -H 'Content-Type: application/json' -d '{}' '{}' ".format(json.dumps(result), callback_url)
      print(cmd)
      os.popen(cmd).read()
    # worker.work()
