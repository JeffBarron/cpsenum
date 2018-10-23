#!/usr/bin/python2
# Author = Jeff Barron
# Critical Path Security Kali IP/Services Enum script
import subprocess
import requests
import os, sys, re

API_ENDPOINT = "http://pastebin.com/api/api_post.php"

# pastebin api key
API_KEY = "d741d64b0a8d88d2c5632b61d14c11a4"

logo = """



             .__  __  .__              .__         
  ___________|__|/  |_|__| ____ _____  |  |        
_/ ___\_  __ \  \   __\  |/ ___\\__  \ |  |        
\  \___|  | \/  ||  | |  \  \___ / __ \|  |__      
 \___  >__|  |__||__| |__|\___  >____  /____/      
     \/                       \/     \/            
              __  .__                              
___________ _/  |_|  |__                           
\____ \__  \\   __\  |  \                          
|  |_> > __ \|  | |   Y  \                         
|   __(____  /__| |___|  /                         
|__|       \/          \/                          
                                  .__  __          
  ______ ____   ____  __ _________|__|/  |_ ___.__.
 /  ___// __ \_/ ___\|  |  \_  __ \  \   __<   |  |
 \___ \\  ___/\  \___|  |  /|  | \/  ||  |  \___  |
/____  >\___  >\___  >____/ |__|  |__||__|  / ____|
     \/     \/     \/                       \/     








"""
WARNING = '\033[93m'
FAILRED = '\033[91m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'
print
logo
print
"CPSEnum has launched."
#    
getIP = subprocess.check_output("ifconfig", stderr=subprocess.STDOUT, shell=True)
ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str(getIP))

ip.insert(0, "*CPS* IP ADDRESSES:")

# Can issue any command and save to pastebin here:
getISSUE = subprocess.check_output("cat /etc/issue", stderr=subprocess.STDOUT, shell=True)
getSERVICES = subprocess.check_output("service --status-all", stderr=subprocess.STDOUT, shell=True)
getNETSTAT = subprocess.check_output("netstat -vnatp", stderr=subprocess.STDOUT, shell=True)

# YUCK CLEAN THIS UP!!
pasteinfo = str(ip) + "\n" + str(getISSUE) + "\n" + str(getSERVICES) + "\n" + str(getNETSTAT)

# pasteinfo = '{0}{1}{2}{3}'.format(ip, getISSUE, getSERVICES, getNETSTAT)

# populate the paste with our shit

thepaste = pasteinfo

data = {'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': thepaste,
        'api_paste_format': 'python'}

# sending post request and saving response as response object 
r = requests.post(url=API_ENDPOINT, data=data)

# extracting response text  
pastebin_url = r.text
print(pasteinfo)
print("The pastebin URL is:%s" % pastebin_url)
# may need to run twice. in testing pastebin has shit the bed once.


# Write file to share
try:
    fo = open("/media/sf_shared/CPSinfo.txt", "w")
    fo.write(thepaste)
    fo.close()
except TypeError as foob:
    print('TypeError:', foob)

except OSError as err:
    print("OSERROR:", err)
    print("Try it with sudo!")

except ValueError as valerr:
    print("ValueERror:", valerr)
print(OKGREEN + "CPSinfo.txt successfully created." + ENDC)
