from flask import Flask,request,jsonify
from urllib.request import urlopen
import json
import requests



app = Flask(__name__)

@app.route("/")
def sayHello():
  return "Hello! I'm Mike. To get the supervisors, please use /getSupervisors. To post, please use /postSupervisor"


@app.route("/api/getSupervisors", methods=['GET'])
def get_supervisors():
  #https://bobbyhadz.com/blog/python-typeerror-the-json-object-must-be-str-bytes-or-bytearray-not-dict#the-json-object-must-be-str-bytes-or-bytearray-not-response000
  response = requests.get("https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers")
  parsed_data = response.json()
  outputDictionary = {}
  #Go through each value in parsed_data
  for x in parsed_data:
    activeLine = (parsed_data[x])
    jurisdiction = activeLine['id']
    lastName = activeLine['lastName']
    firstName = activeLine['firstName'] 

  return(lastIndex)
  # return(parsed_data)


  # response = urlopen("https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers")
  # decoded_reponse = response.read().decode(response)
  # supervisors = json.loads(decoded_response)
  # # id = supervisors[1]
  # print(supervisors)
  # return()



@app.route("/api/postSupervisors", methods=['POST'])
def post_supervisors():
  data = request.get_json()
  return()


if __name__ == "__main__":
  app.run()