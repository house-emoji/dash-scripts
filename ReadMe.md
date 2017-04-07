# Dash Scripts

Dependencies:
Python 3+


phue https://github.com/studioimaginaire/phue
    - sudo pip3 install phue

amazon-dash
    - sudo pip3 install amazon-dash

tcpdump
    - sudo apt-get install tcpdump python-scapy


Argument Documentation
-lights
    A string of the lights name, or a list of light names. Case sensitive.
    -lights "Tyler Living room" "Tyler Hallway" ==> ["Tyler Living room", "Tyler Hallway"]

-groups
    A string of a group name, or a list of group names. Case sensitive.
    -groups "Alex Room" "Tyler Room" ==> ["Alex Room", "Tyler Room"]

-action
    The action you wish the lights+groups to perform. Not case sensitive.
    Actions
        "On"
        "Off"
        "Toggle"    Toggle will either turn the lights OFF, or to the specified color

-color
    The color you want the action to be performed with. Color is in HSV
    0-360  0-254 0-254
      H       S     V
 
-Fade
    How long you want the action to take in seconds


CLI Example:
hue_cli.py -groups "Alex Room" "Hallway" "Living Room" -lights "Tyler Hallway" -action "on" color 180 255 255

How to set up Daemon:
Make sure the permissions on the amazon-dash.yml are the following, or else IT WILL NOT RUN: View content: owner, change content: nobody, execute: nobody
Open the amazon-dash.yml, and add your button, name, and CLI command
Run "sudo amazon-dash run" in the directory with the amazon-dash.yml

