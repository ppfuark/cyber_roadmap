from scapy.all import *
from scapy import *

packet = IP(dst='8.8.8.8')/ICMP()
send(packet)