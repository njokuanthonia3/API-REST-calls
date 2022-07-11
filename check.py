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
reading = reading.to_html('records')

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   
}

payload = json.dumps( {
  "title": "Excel to Table",
  "type": "page",
  "space": {
    "id": "14438105090",
    "name": "Anthonia Oluchukwu Njoku",
    },
  
   
})    

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))