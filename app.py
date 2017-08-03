from flask import Flask
from flask import request
import example
app = Flask(__name__)
import json
@app.route('/')
def homepage():
  q = request.args.get('q')
  return json.dumps(example.parse(q))

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)