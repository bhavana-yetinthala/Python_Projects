# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://team-iuaf8t7ajvj4.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("x","x")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My second jira ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
    "issuetype": {
      "id": "10001"
    },
    
    "project": {
      "key": "SCRUM"
    },
    
    "summary": "My Second Jira Ticket",
    
   
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
