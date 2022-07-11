# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd


url = "https://taiwoojo.atlassian.net/wiki/rest/api/template"
auth = HTTPBasicAuth("email_address", "api_key")
reading = pd.read_excel(r"/Users/mac/Library/Containers/com.microsoft.Excel/Data/Downloads/DATA.xlsx")
reading = reading.to_dict('records')

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",

}

payload = json.dumps( {
  "name": "TestRun",
  "templateType": "page",
  "body": {
    "storage": {
      "value": reading,
      "representation": "view"
    },
    
  }
  
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))