from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
from environs import Env
import psycopg2
import json
import os

app = Flask(__name__)
CORS(app)
heroku = Heroku(app)

conn = psycopg2.connect(
            dbname = "d89m3pip2ct7ar",
            user = "zoviuuhymshtbp",
            password = "dc4d54c8b49a399626258231af673639e4ff2ee7d5f2458598ca0ec83f5f6320",
            host = "ec2-52-7-39-178.compute-1.amazonaws.com",
            port = "5432"
)

# S = "SELECT job, company, salary FROM scraped_info"

cur = conn.cursor()
# res = cur.execute(S)
# list_info = cur.fetchall()
# print(S)

env = Env()
env.read_env()
DATABASE_URL = env("DATABASE_URL")
  # app.config["SQLALCHEMY_DATABASE_URI"] = "http://127.0.0.1:5432/postgresql:/postgres:Hneilson1@localhost/Capstone"


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Job(db.Model):
  __tablename__ = "scraped_info"
  id = db.Column(db.Integer, primary_key=True)
  job = db.Column(db.String(100), nullable=False)
  salary = db.Column(db.String(500))
  company = db.Column(db.String(130))



  def __init__(self, salary, company ):  
    self.salary = salary
    self.company = company


class JobSchema(ma.Schema):
  class Meta:
    fields = ("id", "job",  "salary", "company")

job_schema = JobSchema()
jobs_schema = JobSchema(many=True)

@app.route("/", methods=["GET"])
def home():
  print(S)
  return "<h1>Capstone API</h1>"

# GET
@app.route("/all_job", methods=["GET"])
def all_jobs():
  # all_jobs = jobs_schema.query.all()
  # result = jobs_schema.dump(all_jobs)

  
  print("hello")
  return json.dumps(res)

  # Get one by the id

@app.route("/get_job/<id>", methods=["GET"])
def get_job(id):
   get_job = job.query.get(id)

   result = job_schema.dump(get_job)
   return jsonify(result)


# POST
@app.route("/add-job", methods=["POST"])
def add_job():
  job = request.json["job"]
  salary = request.json["salary"]
  company = request.json["company"]

  new_job = (job, salary, company )

  db.session.add(new_job)
  db.session.commit()

  job = Job.query.get(new_.id)
  return _schema.jsonify()



# DELETE

@app.route("/delete/<id>", methods=["DELETE"])
def remove_job(id):
  record = Job.query.get(id)
  db.session.delete(record)
  db.session.commit()

  return jsonify("delete that ish")



if __name__ == "__main__":
  app.run()