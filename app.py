from flask import Flask,request,jsonify
from urllib.request import urlopen
from operator import itemgetter
# import json
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
  outputList = []
  print(type(parsed_data))  
  for activeLine in parsed_data:
    jurisdiction = activeLine['jurisdiction']
    #Numeric jurisdictions should be excluded from the response
    if not jurisdiction.isdigit():
      lastName = activeLine['lastName']
      firstName = activeLine['firstName'] 
      entry = [jurisdiction, activeLine['lastName'], activeLine['firstName']]
      # https://sparkbyexamples.com/python/create-list-of-lists-in-python/#:~:text=To%20create%20a%20list%20of%20lists%20in%20Python%2C%20you%20can,pop()%20%2C%20and%20del%20statement.
      outputList.append(entry)

  #https://sparkbyexamples.com/python/python-sort-list-of-lists/
  outputList = sorted(outputList, key=itemgetter(1, 2))
  return(outputList)


@app.route("/api/postSupervisors", methods=['POST'])
def post_supervisors():
  data = request.get_json()
  return()


if __name__ == "__main__":
  app.run()