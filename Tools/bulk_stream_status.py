import requests
import json

#check req response then print correct output
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
        res = json.loads(req)
        print('¯\_(ツ)_/¯ '+res["errors"])

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


if __name__ == "__main__":
    main()