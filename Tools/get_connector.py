import requests
import json

#default variables
token = input("Enter user token:")
content_type = 'application/json; charset=utf-8'
headers = {'Authorization': token, 'Content-Type': content_type, 'Accept': 'application/json'}

connector = input("Enter data stream connector id:")

#send post request
hierachy = requests.get('https://app.datorama.com/v1/connectors/{id}'.format(id=connector), headers=headers)

#check if successful call
if hierachy.status_code==200:
    print('\n----------------------------------')
    print("API is working. status code: " + str(hierachy.status_code))
    print('----------------------------------')
    print(hierachy.content)
    
else:
    print("API is not working... status code: " + str(hierachy.status_code))