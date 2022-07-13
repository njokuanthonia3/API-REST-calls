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

auth = HTTPBasicAuth(address, password)

headers = {
   "Accept": "application/json"
}

query = {
   'jql': 'project = AUP',
   'startAt':0,
   'maxResults':50,
   'fields': 'attachment'

}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

result = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
#print(result)

new_file = open('newFile.txt', 'w')
new_file.write(result)


count = 0
result = json.loads(response.text)
for a in result['issues']:
   if a['fields']['attachment'] != []:
      count += 1
   
print(count)



