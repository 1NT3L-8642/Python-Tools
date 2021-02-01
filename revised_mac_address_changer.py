#!/usr/bin/env python

import subprocess

interface = input ("interface > ")
new_mac = input("new MAC > ")

# changed "wlan0" to "interface >", and "00:11:22:33:44:66" to "new MAC" in order to allow the user to put their own variables
# I can change the interface or the new_mac above, and it'll amend itself right throughout the code, instead of me changing it one at a time
# If you want to run this code using python 2, change "input" to "raw_input"


print(" [+] changing MAC address for" + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down ", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up ", shell=True)

# interface is wlan0, and new_mac is 00:11:22:33:44:66, this is because we want to make the changing of the mac address and interface type dynamic.
