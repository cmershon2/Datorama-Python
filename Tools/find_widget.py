import requests
import json

#default variables
token = input("Enter user token:")
content_type = 'application/json; charset=utf-8'
headers = {'Authorization': token, 'Content-Type': content_type, 'Accept': 'application/json'}

workspace_id = input("Enter workspace:")
widget_to_find=[
    #add comma seperated widgets
    88509984,
    88487350
]

widget_counter = 0

#send post request
hierachy = requests.get('https://app.datorama.com/v1/workspaces/{ws}/dashboards/hierarchy'.format(ws=workspace_id), headers=headers)

#check if successful call
if hierachy.status_code==200:
    print('\n----------------------------------')
    print("API is working. status code: " + str(hierachy.status_code))
    print('----------------------------------')
    to_json = hierachy.json()
    all_widgets = to_json['widgets']

    for widget in all_widgets:
        if widget['id'] in widget_to_find:
            page_url = 'https://platform.datorama.com/{ws}/visualize/{pag}/page/v2/{col}'.format(ws=workspace_id,col=widget['pageId'],pag=widget['dashboardId'])
            print("\n- Found widget id: {w_id} on this page: {p_url}".format(w_id=widget['id'],p_url=page_url))
        widget_counter = widget_counter + 1
else:
    print("API is not working... status code: " + str(hierachy.status_code))

print('\n----------------------------------')
print('Job Completed, searched {count} widgets\n'.format(count=widget_counter))