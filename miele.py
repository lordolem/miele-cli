#!/usr/bin/env python3

import requests
import sys
import tokens


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
    'User-Agent': 'github.com/lordolem/miele-cli',
    'Authorization': tokens.auth,
}

params = (
    ('language', 'en'),
)


def pretty_data(machines, building_id):
    print(f"{bcolors.HEADER}-- Grønneviksøren {building_id} --{bcolors.ENDC}")
    for machine in machines:
        unitName = machine['UnitName']
        machineSymbol = machine['MachineSymbol']
        machineColor = machine['MachineColor']
        text1 = machine['Text1']
        text2 = machine['Text2']

        if machineSymbol == 0:
            machineType = f"{bcolors.BGPURPLE}Washer{bcolors.ENDC}"
        else:
            machineType = f"{bcolors.BGCYAN}Dyrer{bcolors.ENDC}"

        if machineColor == 2:
            print(
                f"{bcolors.WARNING}{unitName}{bcolors.ENDC} {machineType}: {bcolors.WARNING}{text1}{text2}{bcolors.ENDC}")
        else:
            print(
                f"{bcolors.OKGREEN}{unitName}{bcolors.ENDC} {machineType}: {bcolors.OKGREEN}{text1}{text2}{bcolors.ENDC}")


def main(bulding_id):
    url_id = "9127"

    if bulding_id == "52":
        url_id = "9126"

    response = requests.get('https://api.mielelogic.com/v3/Country/NO/Laundry/' +
                            url_id + '/laundrystates', headers=headers, params=params)

    # Check reponse status code
    if response.status_code == 200:
        data = response.json()
        machines = [i for i in data['MachineStates']]
        return pretty_data(machines, bulding_id)
    else:
        print(f"{bcolors.FAIL}-- Status code: {response.status_code} --{bcolors.ENDC}")


try:
    machines = main(sys.argv[1])
    building = sys.argv[1]
except IndexError:
    machines = main(54)
    building = "54"
