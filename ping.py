import os
import json
import subprocess

#ip_list = ['8.8.8.8']
#for ip in ip_list:
#    response = os.popen(f"ping {ip}").read()
#    if "Received = 4" in response:
#        print(f"UP {ip} Ping Successful")
#   else:
#       print(f"DOWN {ip} Ping Unsuccessful")


out = open('ping.json', 'a')
subprocess.call(['ping', '8.8.8.8'], stdout=out)
out.close()