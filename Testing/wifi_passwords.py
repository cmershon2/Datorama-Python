#*******************************************************************
# wifi_passwords.py
# Created On:   July 29th, 2021
# Created By:   Casey Mershon
# Version: 0.1
#
# This script will print a list of your saved wifi networks and their
# associated passwords.
#*******************************************************************

import subprocess

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.check_output(['netsh','wlan','show','profiles', i, 'key=clear']).decode('utf-8').split('\n')

    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))