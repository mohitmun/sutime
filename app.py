from flask import Flask
from datetime import datetime
import example
app = Flask(__name__)

@app.route('/')
def homepage():
  the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

  return 

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)