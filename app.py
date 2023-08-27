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
  sortedList = []
  #Pull relevant information from JSON
  for activeLine in parsed_data:
    jurisdiction = activeLine['jurisdiction']
    #Numeric jurisdictions should be excluded from the response
    if not jurisdiction.isdigit():
      # https://sparkbyexamples.com/python/create-list-of-lists-in-python/#:~:text=To%20create%20a%20list%20of%20lists%20in%20Python%2C%20you%20can,pop()%20%2C%20and%20del%20statement.
      entry = [jurisdiction, activeLine['lastName'], activeLine['firstName']]
      sortedList.append(entry)
  
  #Sort Output
  #https://sparkbyexamples.com/python/python-sort-list-of-lists/
  sortedList = sorted(sortedList, key=itemgetter(1, 2))
  for activeLine in sortedList:
    outputList.append(activeLine[0] + " - " + activeLine[1] + ", " + activeLine[2])

  return(outputList)
  # return(parsed_data)


@app.route("/api/postSupervisors", methods=['POST'])
def post_supervisors():
  data = request.get_json()
  return()


if __name__ == "__main__":
  app.run()