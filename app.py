from flask import Flask, jsonify, render_template, request
from database import get_job_by_id, get_jobs_from_db, add_application_to_db

app = Flask(__name__)


@app.route('/')
def hello_world():
  jobs = get_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route("/jobs/<id>")
def show_jobs(id):
  job = get_job_by_id(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)

@app.route("/jobs/<id>/apply", methods=['post']) 
def apply_to_jobs(id):
  data = request.form
  job = get_job_by_id(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', application=data, job=job)

# from flask import render_template

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
