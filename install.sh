#!/usr/bin/env bash

FILE=$HOME/.local/bin/miele

if test -e "$FILE"; then
    sudo rm "$FILE"
    echo "Removing old version..."
fi

sudo cp miele.py $FILE

echo "Installed"