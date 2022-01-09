#!/usr/bin/env bash

FILE=$HOME/.local/bin/miele
OS=`uname`

if [[ $OS == "Darwin" ]]; then
    FILE=/usr/bin/miele
elif [[ $OS == "Linux" ]]; then
  FILE=$HOME/.local/bin/miele
else
    echo "An error has occurred"
    exit 0
fi


if test -e "$FILE"; then
    sudo rm "$FILE"
    echo "Removing old version..."
fi

sudo cp miele.py $FILE

if test -e "$FILE"; then
    echo "Installed successfully"
else
    echo "Something went wrong."
fi