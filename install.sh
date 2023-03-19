#!/usr/bin/env bash

if [ -t 0 ]; then
    # If running in a terminal, continue with the script
    # get USER name
    USER=$(who am i | awk '{print $1}')

    # Set the target file you want to update
    TARGET_FILE="EnvyControlQt.desktop"

    # Get the current working directory
    CURRENT_DIR=$(pwd)

    # Find the actual path of the envycontrol_qt.py file
    ENVYCONTROL_QT_PATH=$(find "$CURRENT_DIR" -type f -name "envycontrol_qt.py" 2>/dev/null | head -n 1)

    # Find the actual path of the envycontrol.png file
    ENVYCONTROL_ICON_PATH=$(find "$CURRENT_DIR" -type f -name "envycontrol.png" 2>/dev/null | head -n 1)

    # Update the Exec and Icon lines in the target file with the actual paths
    sed -i "s|^Exec=.*|Exec=python3 \"${ENVYCONTROL_QT_PATH}\"|" "$TARGET_FILE"
    sed -i "s|^Icon=.*|Icon=${ENVYCONTROL_ICON_PATH}|" "$TARGET_FILE"

    echo "Updated the paths in the $TARGET_FILE"

    # Copy the updated desktop file to /usr/share/applications/
    cp "$TARGET_FILE" /home/$USER/.local/share/applications/

    echo "Copied the $TARGET_FILE to /home/$USER/.local/share/applications/"

    read -p "Press enter to exit script: "
else # Have fun if you have multiple terminals
# I'm tired of trying to make it properly terminal agnostic.
# Without reimplementig bash script in python
    konsole -e "$0"
    gnome-terminal -e "$0"
    xfce4-terminal -e "$0"
    xterm -e "$0"
    terminator -e "$0"
    st -e "$0"
    urxvt -e "$0"
    tilix -e "$0"
    mate-terminal -e "$0"
    kitty -e "$0"
    alacritty -e "$0"
fi
