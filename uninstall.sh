#!/usr/bin/env bash

OS=`uname`

if [[ $OS == "Darwin" ]]; then
    FILE=/usr/local/bin/miele
elif [[ $OS == "Linux" ]]; then
  FILE=$HOME/.local/bin/miele
else
    echo "An error has occurred"
    exit 0
fi


if test -e "$FILE"; then
    sudo rm "$FILE"
    echo "Removed"
fi