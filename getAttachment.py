# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import os
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv

load_dotenv()
password = os.environ.get("APIkey")
address = os.environ.get("email")
url = os.environ.get("url")

new_file = open('newFiles.txt', 'a+')

query = {
      'jql': 'project = AUP',
      'startAt':0,
      'maxResults': 50,
      'fields': 'attachment'
}
count = 0
report = {'startAt': 0, 'total': 1}

while query['startAt'] <  report['total']:

   auth = HTTPBasicAuth(address, password)

   headers = {
      "Accept": "application/json"
   }

   response = requests.request(
      "GET",
      url,
      headers=headers,
      params=query,
      auth=auth
   )

   result = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
   new_file.write(result)

   report = json.loads(response.text)

   for a in report['issues']:
      if a['fields']['attachment'] != []:
         count += 1
   
   query['startAt'] += 50

   

print(count)
   


