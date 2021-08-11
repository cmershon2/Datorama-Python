import requests
import json
token = input("Enter user token:")
workspace = input("Enter workspace:")
update = {"runOnlyAsPartOfWorkflow":False}
content_type = 'application/json; charset=utf-8'
headers = {'Authorization': token, 'Content-Type': content_type, 'Accept': 'application/json'}
num_of_updates = 0

streams = requests.get('https://app.datorama.com/v1/workspaces/{ws}/data-streams'.format(ws=workspace), headers=headers)
failed = []

#check if successful call
if streams.status_code==200:
    print("API is working. status code: " + str(streams.status_code))
    quack = streams.json()
    for counter, stream in enumerate(streams, 1):
        #get each stream from quack
        for method in quack:
            #check if run only as part of workflow is enabled
            if method['runOnlyAsPartOfWorkflow'] is True:
                stream_id = method['id']
                quack = requests.patch('https://app.datorama.com/v1/data-streams/{id}'.format(id=stream_id),headers=headers,json=update)
                print('updated stream: {id}'.format(id=stream_id))
                #increment for aesthetic output :)
                num_of_updates = num_of_updates + 1
else:
    failed.append(streams)
    print("API is not working. status code: " + str(streams.status_code))

if not failed:
    print('Completed job')
    print('Updated: {num} streams'.format(num=num_of_updates))