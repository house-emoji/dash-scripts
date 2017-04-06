Dependencies:
Python 3+

pyphue  https://github.com/rdespoiu/PyPHue
    pip install pyphue

phue https://github.com/studioimaginaire/phue
    pip install phue

amazon-dash
    pip install amazon-dash


pyphue is used ONLY for authentication with the bridge (ocassional) and to get the bridge's current IP address.
All other light operations are done with phue, which has a richer API and is more up to date.


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


Example:
hue_cli.py -groups "Alex Room" "Hallway" "Living Room" -lights "Tyler Hallway" -action "on" color 180 255 255