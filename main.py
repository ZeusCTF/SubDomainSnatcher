#gather subdomains:
"https://blog.appsecco.com/a-penetration-testers-guide-to-sub-domain-enumeration-7d842d5570f6"

import json
import subprocess
from collections import OrderedDict
import argparse

print("""
 ____        _     ____                        _       
/ ___| _   _| |__ |  _ \  ___  _ __ ___   __ _(_)_ __  
\___ \| | | | '_ \| | | |/ _ \| '_ ` _ \ / _` | | '_ \ 
 ___) | |_| | |_) | |_| | (_) | | | | | | (_| | | | | |
|____/ \__,_|_.__/|____/ \___/|_| |_| |_|\__,_|_|_| |_|
/ ___| _ __   __ _| |_ ___| |__   ___ _ __             
\___ \| '_ \ / _` | __/ __| '_ \ / _ \ '__|            
 ___) | | | | (_| | || (__| | | |  __/ |               
|____/|_| |_|\__,_|\__\___|_| |_|\___|_|               
""")

parser = argparse.ArgumentParser(description='Optional app description')

# Gather domain
parser.add_argument('domain', type=str, help='Domain to scan for additional subdomains')
args = parser.parse_args()

subdomains = []

result = subprocess.run(['curl', '-s', f'https://crt.sh/?q={args.domain}&output=json'], stdout=subprocess.PIPE, text=True)
json_data = json.loads(result.stdout)

for num in range(0,len(json_data)):  
    subdomains.append(json_data[num]["name_value"])

# using collections.OrderedDict.fromkeys() to remove duplicated from list
res = list(OrderedDict.fromkeys(subdomains))

for subdomain in res:
    print(subdomain)

