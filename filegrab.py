# SYNTAX FOR KALI = python3 filegrab.py 
#Import the request module that allows for web requests to be made
import requests

url = 'http://websitelocationoffile.com/dir1/dir2/dir3'  # target URL with the directories on, such as image, text files etc
r = requests.get(url, allow_redirects=TRUE) # Allow redirects = TRUE, allows the program to obtain the file even if the web service redirects the user
open('dir1', 'wb').write(r.content) # opens the directory of the target, the downloaded picture for example
