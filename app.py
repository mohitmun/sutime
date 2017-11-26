from flask import Flask
from flask import request
import os
import json
import sys
import json
from rq import Queue
from random import randint
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
  random_id = randint(0,10**10)
  result = q.enqueue(count_words_at_url, query, callback_url, callback_data, random_id, redis_url)
  return json.dumps({'id': random_id})

@app.route('/get')
def homepage():
  id_ = request.args.get('id')
  # callback_data = request.args.get('callback_data')
  # callback_url  = request.args.get('callback_url')
  # random_id = randint(0,10**10)
  # result = q.enqueue(count_words_at_url, query, callback_url, callback_data, random_id, redis_url)
  return json.dumps({'id': id_, 'result': conn.get(id_)})

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)