import pyphue
import argparse
from phue import *

"""
IF YOU NEED TO GET THE USER INFO (Bridge gets reset):
hue = pyphue.PyPHue(wizard=True)

print("IP: ", hue.ip)
print("User: ", hue.user)

# Then paste the user variable into the PyPHue initialization
"""
username = "YcWYkhhe8BUSke0QkAJ07j7VWk5JpTZZEq4CQmiD"  # Update this after a bridge reset
clamp = lambda num, minN, maxN: max(min(maxN, num), minN)  # For keeping numbers within a range

# hue_cli.py -groups "Alex Room" "Hallway" "Living Room" -lights "Tyler Hallway" -action "on" color 255 255 255
#  bridge.set_group("Alex Room", 'on', True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a Light Command")


    parser.add_argument("-groups", "--groups", type=str, nargs='+', default=[],
                        help="List of light groups as written in the hue app. Case sensitive.")

    parser.add_argument("-lights", "--lights", type=str, nargs='+', default=[],
                        help="A list of light names as written in the hue app. Case sensitive.")

    parser.add_argument("-action", "--action", type=str, required=True,
                        help="The action you wish the lights+groups to perform. Not case sensitive.")

    parser.add_argument("-color", "--color", type=int, nargs=3, default=[254, 254, 254],
                        help="The color you want the action to be performed with. Color is in HSV. 360 254 254.")

    parser.add_argument("-fade", "--fade", type=int, default=0,
                        help="How long you want the action to take in seconds")



    args = parser.parse_args()
    # Sanitize inputs
    args.fade *= 10  # Convert from seconds to deciseconds, which phue wants
    args.action = args.action.lower()
    args.color[0] = clamp(int(args.color[0] * 65535.0 / 360.0), 0, 65535)
    args.color[1] = clamp(int(args.color[1]), 0, 254)
    args.color[2] = clamp(int(args.color[2]), 0, 254)

    print("Groups: ", args.groups)
    print("Lights: ", args.lights)
    print("Action: ", args.action)
    print("Color: ", args.color)


    # Connect to the bridge
    bridge_ip = pyphue.PyPHue(user=username).ip
    bridge = Bridge(ip=bridge_ip, username=username)

    setLights = []
    for groupName in args.groups:
        groupLights = bridge.get_group(groupName, 'lights')
        setLights += groupLights

    for lightName in args.lights:
        setLights += bridge.get_light_id_by_name(lightName)

    setLights = list(set(setLights))  # Get rid of duplicates

    setLights = [int(l) for l in setLights]

    # Check the value of a single light, and decide whether to toggle or not from that
    if args.action == 'toggle':
        if bridge.get_light(setLights[0], 'on'):
            args.action = 'off'
        else:
            args.action = 'on'

    command = {'on': args.action=='on',
               'hue': args.color[0],
               'sat': args.color[1],
               'bri': args.color[2],
               'transitiontime': args.fade}

    bridge.set_light(setLights, command)



    #'on' : True|False , 'hue':0-254, 'bri' : 0-254, 'sat' : 0-254, 'ct': 154-500, 'transitiontime': deciseconds,

    # command = {'on'}
    # print("Set Lights: ", setLights)