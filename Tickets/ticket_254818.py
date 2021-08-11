import requests
import json
from datetime import datetime

#default variables
token = input("Enter user token:")
content_type = 'application/json; charset=utf-8'
headers = {'Authorization': token, 'Content-Type': content_type, 'Accept': 'application/json'}
stat_body ={"pageSize": 100,"pageNumber": 1}

workspace=input("Enter workspace:")
streams = requests.get('https://app.datorama.com/v1/workspaces/{ws}/data-streams'.format(ws=workspace), headers=headers)
ga_streams=[]

#check if successful call
if streams.status_code==200:
    print("API is working. status code: " + str(streams.status_code))
    to_json=streams.json()

    for stream in to_json:
        if stream['dataSourceName'] == 'Google Analytics (Manual Mapping)' or stream['dataSourceName'] == 'Google Analytics':
            stats= requests.post('https://app.datorama.com/v1/data-streams/api/{id}/stats'.format(id=stream['id']), headers=headers, json=stat_body)
            if stats.status_code==200:
                to_json_stat=stats.json()
                print('\nData stream id: {id}'.format(id=stream['id']))
                for stat in to_json_stat:
                    start = datetime.strptime(stat['dataStartDate'], '%Y-%m-%d')
                    range_start = datetime.strptime('2021-06-01', '%Y-%m-%d')
                    range_end = datetime.strptime('2021-07-14', '%Y-%m-%d')

                    if range_start<=start<=range_end and stat['status'] != "SUCCESS":
                        print('-- Stat: {id} has a status of {status} and was executed on {st}'.format(id=stat['id'],status=stat['status'],st=stat["dataStartDate"]))
            else:
                print('Failed to retrieve stats')
else:
    print('Failed to retireve streams')

print('Job finished')
