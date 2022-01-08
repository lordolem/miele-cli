#!/usr/bin/env bash

# Colors
FG_RED="\e[91m"
FG_GREEN="\e[92m"
FG_YELLOW="\e[93m"
FG_BLUE="\e[94m"

BG_RED="\e[101m"
BG_GREEN="\e[102m"
BG_YELLOW="\e[103m"
BG_BLUE="\e[104m"
BG_CYAN="\e[106m"
BG_GRAY="\e[100m"

NC="\e[0m"
###########

function getLaundryState() {

  if [[ $1 == 52 ]]; then
    ID="9126"
  elif [[ $1 == 54 ]]; then
    ID="9127"
  fi

  laundryState=$(curl "https://api.mielelogic.com/v3/Country/NO/Laundry/$ID/laundrystates?language=en" \
  -H 'Authorization: ' \
  --compressed -s)

  length=$(echo "$laundryState" | jq ".MachineStates" | jq "length")
  length=$((length-1))

  for i in $(seq 0 $length); do
    unitName=$(echo "$laundryState" | jq ".MachineStates[$i].UnitName")
    machineSymbol=$(echo "$laundryState" | jq ".MachineStates[$i].MachineSymbol")
    machineColor=$(echo "$laundryState" | jq ".MachineStates[$i].MachineColor")
    text1=$(echo "$laundryState"  | jq ".MachineStates[$i].Text1" | sed -e 's/\\n//g')
    text2=$(echo "$laundryState"  | jq ".MachineStates[$i].Text2" | sed -e 's/\\n//g')

    if [[ $machineSymbol == 0 ]]; then
      type="${BG_GRAY}Washer${NC}"
    else
      type="${BG_BLUE}Dyrer${NC}"
    fi

    if [[ $machineColor == 2 ]]; then
      echo -e "${FG_RED}$unitName ${NC}$type:-${FG_RED} $text1 $text2${NC}" | sed "s/\"//g"
    else
      echo -e "${FG_GREEN}$unitName ${NC}$type:-${FG_GREEN} $text1 $text2${NC}" | sed "s/\"//g"
    fi
  done
}

case "$1" in
  "help")
    echo "Usage: miele [52|54]"
    exit 0
    ;;
  "52")
    echo -e "${FG_GREEN}-- Grønneviksøren $1 --${NC}"
    getLaundryState 52 | column -t -s "-" 
    exit 0
    ;;
  "54")
    echo -e "${FG_GREEN}-- Grønneviksøren $1 --${NC}"
    getLaundryState 54 | column -t -s "-" 
    exit 0
    ;;
  *)
    echo -e "${FG_GREEN}-- Grønneviksøren 54 --${NC}"
    getLaundryState 54 | column -t -s "-" 
    exit 0
    ;;
esac
