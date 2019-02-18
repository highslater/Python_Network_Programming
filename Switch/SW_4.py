#!/usr/bin/env python3


##SW_4.py

import getpass
import telnetlib

#####Enter LOGIN Credentials

HOST = input("Enter HOST ADDRESS: ")
user = input("Enter your remote account: ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#####Configure Default Security Settings

tn.write(b"conf t\n")
tn.write(b"no ip routing\n")
tn.write(b"enable secret cisco\n")
tn.write(b"username S4ccna privilege 15 password S4cisco\n")
tn.write(b"ip domain-lookup\n")
tn.write(b"ip name-server 192.168.122.1\n")
tn.write(b"http server\n")
tn.write(b"ip domain-name gns3.com\n")
tn.write(b"line console 0\n")
tn.write(b"logging synchronous\n")
tn.write(b"exec-timeout 0 0\n")
tn.write(b"login local\n")
tn.write(b"line vty 0 4\n")
tn.write(b"logging synchronous\n")
tn.write(b"exec-timeout 0 0\n")
tn.write(b"login local\n")
tn.write(b"line aux 0\n")
tn.write(b"logging synchronous\n")
tn.write(b"exec-timeout 0 0\n")
tn.write(b"login local\n")
tn.write(b"exit\n")

#####Create 10 vlans and MANAGEMENT Vlan
for n in range(2, 11):
	num = str(n).encode('ascii') + b"\n"
	tn.write(b"vlan " + num)
	tn.write(b"name vlan__" + num)

tn.write(b"vlan 99\n")
tn.write(b"name MANAGEMENT\n")

#####Configure ALL Connected Ports

tn.write(b"interface e0/0\n")
tn.write(b"description MANAGEMENT PORT TO SW_1\n")
tn.write(b"no shutdown\n")

tn.write(b"interface e0/1\n")
tn.write(b"description PRODUCTION PORT TO SW_2\n")
tn.write(b"no shutdown\n")

tn.write(b"interface e0/2\n")
tn.write(b"description PRODUCTION PORT TO SW_3\n")
tn.write(b"no shutdown\n")

#####Shutdown ALL Unused Ports
tn.write(b"interface range e0/3, e1/0 - 3, e2/0 - 3, e3/0 - 3\n")
tn.write(b"description SHUTDOWN as Security Best Practice\n")
tn.write(b"shutdown\n")

#####Configure vlan 99
tn.write(b"interface vlan 99\n")
tn.write(b"ip address 192.168.122.153 255.255.255.0\n")
tn.write(b"description MANAGEMENT VLAN 99\n")
tn.write(b"no shutdown\n")

#####Shutdown and SECURE vlan 1
tn.write(b"interface vlan 1\n")
tn.write(b"no ip address\n")
tn.write(b"description SHUTDOWN as Security Best Practice\n")
tn.write(b"shutdown\n")


#####Exit, Copy Configuration, and LOGOUT

tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"cop r s\n")
tn.write(b"\n")
tn.write(b"exit\n")
tn.write(b"logout\n")

#####Output: >>>>> Commands Entered

print("\n\n\n*** START ***")
print(tn.read_all().decode('ascii'))
print("*** COMPLETE ***\n\n\n")

