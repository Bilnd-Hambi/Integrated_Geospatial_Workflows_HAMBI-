# WPS Execute Operation
 
import requests, os

payload = open(os.path.dirname(os.path.abspath(__file__)) + r"\xml\length_calculation.xml").read()
 
API_URL = "https://mara.rangelands.itc.utwente.nl/geoserver/ows"

response = requests.post(API_URL, data=payload)
print("Content-type: application/json")
print()
print(response.text)