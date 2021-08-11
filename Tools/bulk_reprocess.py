import requests
import json

#check req response then print correct output
def errorHandler(req):
    print('─────────────────────')
    if req.status_code==200:
        print("\nStatus code: " + str(req.status_code))
        print('\nProcessing Started')
        print('─────────────────────')
        print(req.content)
    else:
        print('\nJob failed:')
        res = json.loads(req)
        print('¯\_(ツ)_/¯ '+res["errors"])

#main function
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

    #check platfomr & send post request
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

#used to check if script is being imported or ran directly
if __name__ == '__main__':
    main()