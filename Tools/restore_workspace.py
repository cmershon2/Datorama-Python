import requests
import json

token= ""
workspace_id=""

headers= {'token':token}

url= 'https://app.datorama.com/services/admin/restore/byidandtype?entityId={ws}&entityType=Brand'.format(ws=workspace_id)

res= requests.post(url, headers=headers)

print(res.status_code)