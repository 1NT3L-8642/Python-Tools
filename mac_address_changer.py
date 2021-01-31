------------------------------------------------------------------------#script1 --------------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python


import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)

-------------------------------------------------------------------------#script2 ----------------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python


import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:66"
# I can change the interface or the new_mac above, and it'll amend itself right throughout the code, instead of me changing it one at a time

print(" [+] changing MAC address for" + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + "  hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

# interface is wlan0, and new_mac is 00:11:22:33:44:66, this is because we want to make the changing of the mac address and interface type dynamic.
