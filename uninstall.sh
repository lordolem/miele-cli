#!/usr/bin/env bash

OS=`uname`

if [[ $OS == "Darwin" ]]; then
    FILE=/usr/local/bin/miele
elif [[ $OS == "Linux" ]]; then
    FILE=$HOME/.local/bin/miele
else
    echo "An error has occurred"
    exit 1
fi


if [[ -e "$FILE" ]]; then
    sudo rm "$FILE"
    echo "Removed miele from system"
fi