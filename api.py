import requests
url = "http://sandboxapicdc.cisco.com"
body = "{\"aaaUser\" : {\"attributes\" : {\"name\": \"admin\",\"pwd\": \"ciscopsdt\"}}}"
headers = {"Content-type":"application/json"}
resp = requests.post(url=url,data=body, headers=headers, verify=False)
print(resp.text)