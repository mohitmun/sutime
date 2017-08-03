from flask import Flask
from flask import request
import os
import json
import sys
import json
from rq import Queue
# from worker import conn
import redis
from utils import count_words_at_url
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
q = Queue(connection=conn)
app = Flask(__name__)

@app.route('/')
def homepage():
  query = request.args.get('q')
  callback_data = request.args.get('callback_data')
  callback_url  = request.args.get('callback_url')
  result = q.enqueue(count_words_at_url, query, callback_url, callback_data)
  return json.dumps({})

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)