"""
Author: Patrick Marchione
Class: CSEC 473 Cyber Defense Techniques
Assignment: Homework 3 - Red Team Tools
Description: The purpose of this tool is to determine
the OS that the target machine is running and to return
and known vulnerabilites that may be exploited on that
machine

Usage: 
[WINDOWS] python.exe recon.py target_ip
[UNIX] python recon.py target_ip
"""
import os
import sys
import requests

target = sys.argv[1]
#target = '127.0.0.1'
os.system(f"nmap -O {target} > recon.txt")
os.system(f"echo Vulnerabilites: >> recon.txt")

#Determines which data from the nmap scan will be tested
flip = False
services = []
file = open("recon.txt", 'r')
for line in file:
    line = line.strip().split()

    if line == []:
        continue

    if (line[0] == "Device" or line[0] == "No") and line != []:
        flip = False

    if flip and line != []:
        services.append(line[2])

    if line[0] == "PORT" and line != []:
        flip = True   
file.close()

#Uses the open ports and their services and provides links to the NIST vulnerability database
file = open("recon.txt", "a")
for service in services:
    reponse = requests.get(f"https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={service}&search_type=all&isCpeNameSearch=false")
    if reponse.status_code == 200:
        file.write(f"{service}: https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={service}&search_type=all&isCpeNameSearch=false\n")
file.close()