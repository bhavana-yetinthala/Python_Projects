import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])

def createJira():

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
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "AB"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


app.run(host='0.0.0.0', port=5000)