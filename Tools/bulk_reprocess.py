#*******************************************************************
# bulk_reprocess.py
# Created On:   July 13th, 2021
# Created By:   Casey Mershon
# Version: 0.1
#
# The bulk_reprocess.py script will reprocess a given array of data
# stream ids. This script requires a user session token (can be
# retrieved from the profile settings in Datoram), the start date,
# the end date, the platform (ie. us1, eu1), and a comma seperated
# list of of data stream ids. The list of stream ids will need to 
# be added into main() function.
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
        print('─────────────────────\n')
        print(req.content)
    else:
        print("\nStatus code: " + str(req.status_code))
        print('\nJob failed:')
        print('─────────────────────\n')
        res = json.loads(req)
        print('¯\_(ツ)_/¯ \n'+res["errors"])

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

    #define processing data
    #format YYYY-MM-DD
    startDate= input("\nEnter start date in 'YYYY-MM-DD' format:")
    endDate=input("\nEnter end date in 'YYYY-MM-DD' format:")
    streams=[
        #Add streams
    ]

    print("Platforms:\n 1 | us1\n 2 | us2\n 3 | eu1\n 4 | eu2\n")
    platform = input("Platform: ")

    #build request body
    body={
        "dataStreamIds":streams,
        "startDate": startDate,
        "endDate": endDate,
        "create": False
    }

    #check platform & send post request
    if platform=='1':
        req = requests.post('https://app.datorama.com/v1/data-streams/process', headers=headers, json=body)
        errorHandler(req)
    elif platform=='2':
        req = requests.post('https://app-us2.datorama.com/v1/data-streams/process', headers=headers, json=body)
        errorHandler(req)
    elif platform=='3':
        req = requests.post('https://app-eu.datorama.com/v1/data-streams/process', headers=headers, json=body)
        errorHandler(req)
    elif platform=='4':
        req = requests.post('https://app-eu2.datorama.com/v1/data-streams/process', headers=headers, json=body)
        errorHandler(req)

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