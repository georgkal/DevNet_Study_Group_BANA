import requests
from pprint import pprint


url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

payload="{\n    \"aaaUser\" : {\n        \"attributes\" : {\n            \"name\" : \"admin\",\n            \"pwd\" : \"ciscopsdt\"\n        }\n    }\n}"
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

#pprint(response.text)
pprint(response.headers)