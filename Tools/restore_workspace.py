import requests
import json

token = input("Enter user token:")
workspace_id= input("\nEnter workspace id:")

headers= {'token':token}

url= 'https://app.datorama.com/services/admin/restore/byidandtype?entityId={ws}&entityType=Brand'.format(ws=workspace_id)

res= requests.post(url, headers=headers)

print(res.status_code)