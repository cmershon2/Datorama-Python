#*******************************************************************
# find_widget.py
# Created On:   July 13th, 2021
# Created By:   Casey Mershon
# Version: 0.1
#
# The find_widget.py script will find a given array of widget ids.
# This script requires a user session token (can be retrieved from 
# the profile settings in Datoram), the start date, the end date, 
# the platform (ie. us1, eu1), and a comma seperated list of 
# of widget ids. The list of widget ids will need to be added into
# main() function.
#*******************************************************************
# Dependancies:
#   - pip install requests
#   ---- https://pypi.org/project/requests/
#   (JSON import is a built-in module)
#*******************************************************************
# Available script functions:
#   - def main()
#   - def errorHandler(req)
#*******************************************************************

import requests
import json

#*******************************************************************
# 
# errorHandler(req)
#
# This function is responsible for outputing the response from the 
# API call. This will inform users if the API call was successful or
# if the failed. Additionally, the full responce will be output.
#
#*******************************************************************
def errorHandler(req, widget_to_find, workspace_id):
    widget_counter = 0
    print('─────────────────────')
    OKCYAN = '\033[96m'
    CEND='\033[0m'
    if req.status_code==200:
        print("\nStatus code: " + str(req.status_code))
        print('\nJob Started')
        print('─────────────────────')
        to_json = req.json()
        all_widgets = to_json['widgets']

        for widget in all_widgets:
            if widget['id'] in widget_to_find:
                page_url = 'https://platform.datorama.com/{ws}/visualize/{pag}/page/v2/{col}'.format(ws=workspace_id,col=widget['pageId'],pag=widget['dashboardId'])
                print("\n- Found widget id: {w_id} on this page: {cs}{p_url}{ce}".format(w_id=widget['id'],p_url=page_url, cs=OKCYAN, ce=CEND))
            widget_counter = widget_counter + 1
    else:
        print("\nStatus code: " + str(req.status_code))
        print('\nJob failed:')
        print('─────────────────────\n')
        res = req.json()
        print('¯\_(ツ)_/¯')
        print(res)

    print('─────────────────────\n')
    print('Job Completed, searched {count} widgets\n'.format(count=widget_counter))

#*******************************************************************
# 
# main()
#
# This function is responsible for gathering input from command line
# for the token, start date, end date, and platform. The streams will
# need to be manually entered in the script and saved. After inputs 
# are collected, the requests are sent to the proper platform. Once
# a response is returned, it is sent to the errorHandler function.
#
#*******************************************************************
def main():
    #default variables
    token = input("Enter user token:")
    content_type = 'application/json; charset=utf-8'
    headers = {'Authorization': token, 'Content-Type': content_type, 'Accept': 'application/json'}

    workspace_id = input("Enter workspace:")
    print("Platforms:\n 1 | us1\n 2 | us2\n 3 | eu1\n 4 | eu2\n")
    platform = input("Platform: ")
    widget_to_find=[
        #add comma seperated widgets
    ]

    #check platform & send post request
    if platform=='1':
        req = requests.get('https://app.datorama.com/v1/workspaces/{ws}/dashboards/hierarchy'.format(ws=workspace_id), headers=headers)
        errorHandler(req, widget_to_find, workspace_id)
    elif platform=='2':
        req = requests.get('https://app-us2.datorama.com/v1/workspaces/{ws}/dashboards/hierarchy'.format(ws=workspace_id), headers=headers)
        errorHandler(req, widget_to_find, workspace_id)
    elif platform=='3':
        req = requests.get('https://app-eu.datorama.com/v1/workspaces/{ws}/dashboards/hierarchy'.format(ws=workspace_id), headers=headers)
        errorHandler(req, widget_to_find, workspace_id)
    elif platform=='4':
        req = requests.get('https://app-eu2.datorama.com/v1/workspaces/{ws}/dashboards/hierarchy'.format(ws=workspace_id), headers=headers)
        errorHandler(req, widget_to_find, workspace_id)

#*******************************************************************
# 
# Simple guard clause to check if script is being ran by itself or 
# if the script is being imported to a seperate script. This ensures
# the main() function is not ran by default when importing it to an
# external scipt.
#
#*******************************************************************
if __name__ == '__main__':
    main()