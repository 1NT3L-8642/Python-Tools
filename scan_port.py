# These modules need to be imported to allow the code to run
import sys
import socket
import pyfiglet # This module creates the artistic banner, this may need importing seperately from Kali.

# The artistic banner that will show up before the tool does its' work
ascii_banner = pyfiglet.figlet_format("Scan_Port \n Open Port Scanner")
print(ascii_banner)


ip = 'IP ADDRESS' # Input the target IP address here
open_ports =[] # The [] here will be populated with the results of our scan

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!! Choose one of the below, when running the code, comment the other one out using # !!!

# OPTION 1 - Check all ports
ports = range(1, 65535) # Anything between port 1 and 65535 will be checked

# OPTION 2 - Specify exactly what ports you want to scan
ports = {21, 22, 23, 53, 80, 135, 443, 445} #These are the most common ports that would be open, try this first, if not, do OPTION 1.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# This will try to connect to the port, if it succeeds, then the port is open and will show in the results
def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result

# This is a for loop which will allow the program to keep repeating until all desired prots have been checked
for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    
# Results, if the ports are open, show in terminal
if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports))
# if not, print a message for the user
else: 
  print ("Looks like no ports are open :(")
