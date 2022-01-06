FILE=/usr/bin/miele

if test -e "$FILE"; then
    sudo rm "$FILE"
    echo "Removing old version..."
fi

sudo cp miele.py /usr/bin/miele