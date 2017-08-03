from flask import Flask
from flask import request
import os
import json
from sutime import SUTime
import sys
import json
app = Flask(__name__)
jar_files = os.path.join(os.path.dirname(__file__), 'jars')
sutime = SUTime(jars=jar_files, mark_time_ranges=False)
@app.route('/')
def homepage():
  q = request.args.get('q')
  return json.dumps(parse(q))
def parse(s):
  return sutime.parse(s)
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)