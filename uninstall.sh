#!/usr/bin/env bash

FILE=$HOME/.local/bin/miele

if test -e "$FILE"; then
    echo "Removing old version..."
    sudo rm "$FILE"
fi