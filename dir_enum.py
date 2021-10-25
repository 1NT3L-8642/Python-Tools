# Import these to allow the code to run
import requests
import sys

# The chosen wordlist should contain common directory names, such as dir, login, connections, robots; this wordlist can be custom
sub_list = open(wordlist.txt).read() # wordlist.txt should be replaced with the name of the actual wordlist you want to use
directories = sub_list.splitlines()

# The below represetns the structure of the web address, that can be interrogated to find directories
for dir in directories
  dir_enum = f"http://{sys.argv[1]}/{dir}.html 
  r = requests.get(dir_enum)
  if r.status_code==404: # directories are found using web requests, if 404, the program will ignore it, as we can't use it
    pass
  else:
    print("Valid Directory:" ,dir_enum)

#  SYNTAX IN KALI = python3 dir_enum.py IP ADDRESS
