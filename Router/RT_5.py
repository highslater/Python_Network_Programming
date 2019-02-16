##RT_5


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
tn.write(b"hostname RT_5\n")
tn.write(b"interface loopback1\n")
tn.write(b"ip address 1.1.1.5 255.255.255.255\n")
tn.write(b"interface loopback2\n")
tn.write(b"ip address 2.2.2.5 255.255.255.255\n")
tn.write(b"interface loopback3\n")
tn.write(b"ip address 3.3.3.5 255.255.255.255\n")
tn.write(b"interface loopback4\n")
tn.write(b"ip address 4.4.4.5 255.255.255.255\n")
tn.write(b"interface loopback5\n")
tn.write(b"ip address 5.5.5.5 255.255.255.255\n")
tn.write(b"exit\n")
tn.write(b"router ospf 110\n")
tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"cop r s\n")
tn.write(b"\n")
tn.write(b"exit\n")
print("\n\n\n*** START ***")
print(tn.read_all().decode('ascii'))
print("*** COMPLETE ***\n\n\n")

