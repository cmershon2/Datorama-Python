#*******************************************************************
# bulk_stream_status.py
# Created On:   August 23rd, 2021
# Created By:   Casey Mershon
# Version: 0.1
#
# The bulk_stream_status.py script will output the stream's id, it's
# run status, and if the stream is enabled/disabled. This script 
# requires a user session token (can be retrieved from the profile 
# settings in Datoram), the start date, the end date, the platform 
# (ie. us1, eu1), and a comma seperated list of of data stream ids.
# The list of stream ids will need to be added into main() function.
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
def errorHandler(req):
    print('─────────────────────')
    if req.status_code==200:
        print("\nStatus code: " + str(req.status_code))
        print('\nJob Started')
        print('─────────────────────')
        to_json = req.json()
        for s in to_json:
            CRED='\033[91m'
            CGREEN = '\033[92m'
            CEND='\033[0m'

            if s["runStatus"] == "FAILURE" and s["status"] == "DISABLED":
                print("{s} | Run Stat: {cs}{rs}{ce} | Stat: {cs}{ss}{ce} ".format(s=s["id"], rs=s["runStatus"], ss=s["status"], cs=CRED, ce=CEND))
            elif s["status"] == "DISABLED":
                print("{s} | Run Stat: {rs} | Stat: {cs}{ss}{ce} ".format(s=s["id"], rs=s["runStatus"], ss=s["status"], cs=CRED, ce=CEND))
            elif s["runStatus"] == "FAILURE":
                print("{s} | Run Stat: {cs}{rs}{ce} | Stat: {ss}".format(s=s["id"], rs=s["runStatus"], ss=s["status"], cs=CRED, ce=CEND))
            else:
                print("{s} | Run Stat: {cs}{rs}{ce} | Stat: {cs}{ss}{ce}".format(s=s["id"], rs=s["runStatus"], ss=s["status"], cs=CGREEN, ce=CEND))
    else:
        print('\nJob failed:')
        res = req.json()
        print('¯\_(ツ)_/¯')
        print(res)

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
    token = input("\nEnter user token: ")
    workspace = input("\nEnter Workspace Id: ")
    print("\nPlatforms:\n 1 | us1\n 2 | us2\n 3 | eu1\n 4 | eu2\n")
    platform = input("Platform: ")
    #format YYYY-MM-DD
    startDate= input("\nEnter start date in 'YYYY-MM-DD' format:")
    endDate=input("\nEnter end date in 'YYYY-MM-DD' format:")
    content_type = 'application/json; charset=utf-8'
    headers = {'Authorization': token, 'Content-Type': content_type, 'Accept': 'application/json'}
    body = str({
        "startDate": startDate, 
        "endDate": endDate
    })
    streams = [
        #enter stream list
    ]
    #combine streams into comma seperated string
    sList = ",".join([str(element) for element in streams])

    #check platform & send get request
    if platform=='1':
        req = requests.get('https://app.datorama.com/v1/workspaces/{ws}/data-streams/status/bulk?ids={streamList}'.format(ws=workspace, streamList=sList), headers=headers, data=body)
        errorHandler(req)
    elif platform=='2':
        req = requests.get('https://app-us2.datorama.com/v1/workspaces/{ws}/data-streams/status/bulk?ids={streamList}'.format(ws=workspace, streamList=sList), headers=headers, data=body)
        errorHandler(req)
    elif platform=='3':
        req = requests.get('https://app-eu.datorama.com/v1/workspaces/{ws}/data-streams/status/bulk?ids={streamList}'.format(ws=workspace, streamList=sList), headers=headers, data=body)
        errorHandler(req)
    elif platform=='4':
        req = requests.get('https://app-eu2.datorama.com/v1/workspaces/{ws}/data-streams/status/bulk?ids={streamList}'.format(ws=workspace, streamList=sList), headers=headers, data=body)
        errorHandler(req)

#*******************************************************************
# 
# Simple guard clause to check if script is being ran by itself or 
# if the script is being imported to a seperate script. This ensures
# the main() function is not ran by default when importing it to an
# external scipt.
#
#*******************************************************************
if __name__ == "__main__":
    main()