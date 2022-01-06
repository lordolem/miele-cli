#!/usr/bin/python

import requests
import sys

class bcolors:
    HEADER = '\033[4m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BGPURPLE = '\033[45m'
    BGCYAN = '\033[44m'
    ENDC = '\033[0m'

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': '',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Sec-GPC': '1',
    'Origin': 'https://mielelogic.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://mielelogic.com/',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = (
    ('language', 'en'),
)

def get_data(bulding_id):
    if bulding_id == "52":
        url_id = "9126"
    elif bulding_id == "54":
        url_id = "9127"
    else:
        url_id = "9127"
    
    response = requests.get(f'https://api.mielelogic.com/v3/Country/NO/Laundry/{url_id}/laundrystates', headers=headers, params=params)
    data = response.json()
    machines = [i for i in data['MachineStates']]

    return machines

try:
    machines = get_data(sys.argv[1])
    building = sys.argv[1]
except IndexError:
    machines = get_data(54)
    building = "54"

print(f"{bcolors.HEADER}-- Grønneviksøren {building} --{bcolors.ENDC}")

for machine in machines:
    unitName = machine['UnitName']
    machineSymbol = machine['MachineSymbol']
    machineColor = machine['MachineColor']
    text1 = machine['Text1']
    text2 = machine['Text2']
    
    if machineSymbol == 0:
        machineType=f"{bcolors.BGPURPLE}Washer${bcolors.ENDC}"
    else:
        machineType=f"{bcolors.BGCYAN}Dyrer${bcolors.ENDC}"

    if machineColor == 2:
        print(f"{bcolors.WARNING}{unitName}{bcolors.ENDC} {machineType}: {bcolors.WARNING}{text1}{text2}{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKGREEN}{unitName}{bcolors.ENDC} {machineType}: {bcolors.OKGREEN}{text1}{text2}{bcolors.ENDC}")
        