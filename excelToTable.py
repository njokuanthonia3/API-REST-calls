# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import os
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
password = os.environ.get("APIkey")
address = os.environ.get("email")


url = "https://taiwoojo.atlassian.net/wiki/rest/api/content"
auth = HTTPBasicAuth(address, password)
reading = pd.read_excel(r"/Users/mac/Library/Containers/com.microsoft.Excel/Data/Downloads/DATA.xlsx")
reading = reading.to_html(index=False)

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   
}

payload = json.dumps( {
  "title": "Excel to Table4",
  "type": "page",
  "space": {
    "id": "14438105090",
    "name": "Anthonia Oluchukwu Njoku"
    },
    "body": {
    "storage": {
      "value": reading,
      "representation": "storage"
    }
    }
} )    

response = requests.request(

   "POST",
   url,
   auth=auth,
   data=payload,
   headers=headers
)

#print(response.text)
print(response.status_code)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

with open('response.txt', 'w') as rules:
  rules.write(response.text)

