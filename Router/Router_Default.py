##Router_Default


import getpass
import telnetlib

HOST = input("Enter HOST ADDRESS: ")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"enable secret cisco\n")
tn.write(b"username ccna privilege 15 password cisco\n")
tn.write(b"ip domain-lookup\n")
tn.write(b"ip name-server 192.168.122.1\n")
tn.write(b"http server\n")
tn.write(b"ip domain-name gns3.com\n")


#tn.write(b"crypto key zeroize\n")
#tn.read_until(b"[yes/no]: ")
#tn.write(b"yes\n")
#tn.write(b"crypto key generate rsa modulus 2056\n")
#tn.write(b"ip ssh version 2\n")

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
tn.write(b"exit\n")
tn.write(b"cop r s\n")
tn.write(b"\n")
tn.write(b"exit\n")
print("\n\n\n*** START ***")
print(tn.read_all().decode('ascii'))
print("*** COMPLETE ***\n\n\n")

