from flask import Flask, render_template
from database import get_jobs_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
  jobs = get_jobs_from_db()
  return render_template('home.html', jobs=jobs)


# from flask import render_template

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
