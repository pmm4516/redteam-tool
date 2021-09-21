# redteam-tool
CSEC 473 homework 3 Red Team Tool

Description
This tool is used for recon. It will detect the operating system of the target machine and if there are any open ports on the machine. It will then provide links to the NIST vulnerability database for the services and ports that are open.

Requirements:
Python is required to run the tool.
The python requests module is also required and can be installed easily through the command: _pip install requests_.
Nmap is also required and can installed through the link https://nmap.org/download.html [WINDOWS] or through the command _sudo apt install nmap_ for Debian distros.

Usage:
To run the tool, in either powershell or terminal, run the command 
  [WINDOWS] python.exe recon.py _target_ip_
  [UNIX] python recon.py _target_ip_
  
  example: python.exe recon.py 127.0.0.1
