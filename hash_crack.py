# SYNTAX FOR KALI = python3 hash_crack.py
# python has a library for hashes, so lets import it
import hashlib
import pyfiglet # The artistic banner

ascii_banner = pyfiglet.figlet_format("HashCrack \n PasswdSafe = FALSE") # Prints the banner
print(ascii_banner)

# We need to specify the wordlist location that contains the hashes that need cracking
wordlist_location = str(input('Enter wordlist file location: '))
hash_input = str(input('Enter hash to be cracked: ')) # Here we enter the chosen hash


with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        hash_ob = hashlib.md5(line.strip().encode()) # The hashlib.md5 specifies that we want to interrograte the hashes as being md5 (feel free to change to SHA256 etc)
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print('Found cleartext password! ' + line.strip())
            exit(0)
