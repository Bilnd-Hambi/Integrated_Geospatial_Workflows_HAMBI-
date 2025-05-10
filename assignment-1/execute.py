# WPS Execute Operation
 
import requests, os

payload = open(os.path.dirname(os.path.abspath(__file__)) + r"\\xml\\area.xml").read()
 
BASES_SERVER_URL = "https://gisedu.itc.utwente.nl/student/s3559386/gpw/assignment-1/api"
API_URL = (BASES_SERVER_URL+"/wps.py?")



response = requests.post(API_URL, data=payload)
print("Content-type: application/json")
print()
print(response.text)