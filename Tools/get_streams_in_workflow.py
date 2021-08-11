import requests
import json

token = input("Enter user token:")
content_type = 'application/json; charset=utf-8'
headers = {'Authorization': token, 'Content-Type': content_type, 'Accept': 'application/json'}

workflow_id = input("Enter workflow id:")

workflow = requests.post('https://app.datorama.com/services/admin/workflow/find/{wf}'.format(wf=workflow_id), headers=headers)
