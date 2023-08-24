#!/bin/python

from flask import Flask,request,jsonify
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route("/")
def sayHello():
  return "Hello! I'm Mike. To get the supervisors, please use /getSupervisors. To post, please use /postSupervisor"


@app.route("/api/getSupervisors", methods=['GET'])
def get_supervisors():
  url = "https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers"
  """response = json.loads(request.gett("GET",url).text)"""
  response = urlopen(url)
  """return response"""
  """Single line: {"id":"1","phone":"204-798-9969","jurisdiction":"u","identificationNumber":"d4900a18-a304-42c6-a8e5-a6c8c3f17bc0","firstName":"Karson","lastName":"Olson"}"""
  data_json = json.loads(response.read())
  print(type(data_json))
  return()
 
 
 
  """JAIL
  print(data_json)
  """

if __name__ == "__main__":
  app.run()