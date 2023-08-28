from flask import Flask,request,url_for,redirect,render_template
from operator import itemgetter
import requests



app = Flask(__name__)

@app.route("/")
def sayHello():
  return "Hello! I'm Mike. To get the supervisors, please use /api/getSupervisors. To post, please use /api/postSupervisor"


@app.route("/api/getSupervisors", methods=['GET'])
def get_supervisors():
  response = requests.get("https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers") # Pull down list of managers
  parsed_data = response.json()
  sortedList = []
  outputList = []
  #Pull relevant information from JSON
  for activeLine in parsed_data:
    jurisdiction = activeLine['jurisdiction']
    if not jurisdiction.isdigit(): #numeric jurisdictions should be excluded from the response
      entry = [jurisdiction, activeLine['lastName'], activeLine['firstName']]
      sortedList.append(entry)
  #Sort Output
  sortedList = sorted(sortedList, key=itemgetter(0, 1, 2)) # Sorted in alphabetic order by jurisdiction, lastName, firstName
  for activeLine in sortedList:
    outputList.append(activeLine[0] + " - " + activeLine[1] + ", " + activeLine[2]) # "jurisdiction - lastName, firstName"
  return(outputList)


@app.route("/api/postSupervisors", methods=['POST','GET'])
def post_supervisors():
  if request.method == "POST":
      firstName = request.form['firstName'] #required
      lastName  = request.form['lastName'] #required
      email = request.form['email']
      phoneNumber  = request.form['phoneNumber']
      supervisor = request.form['supervisor'] #required
      output = firstName + " " + lastName + " " + email + " " + phoneNumber + " " + supervisor
      print(output) #Printed to the console upon receiving the post request
      return(output)
  else:
    return render_template("postSupervisors.html")

if __name__ == "__main__":
  app.run()