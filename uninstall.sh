FILE=/usr/bin/miele

if test -e "$FILE"; then
    echo "Removing old version..."
    sudo rm "$FILE"
fi