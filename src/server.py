'''
COMP 8505 - Assignment 1
Cover Channel - Server by Jeffrey Sasaki

This python program acts as a listener for covert traffic coming into the
machine

The program listens for traffic and listens for the "Echo" flag bit
It then reads the data from the source port.
'''

import sys
from scapy.all import *

# Listens and filter covert traffic, denoted with an "E" flag
def parse(pkt):
	flag=pkt['TCP'].flags
	if flag == 0x40:
		char = chr(pkt['TCP'].sport)
	        sys.stdout.write(char)

# Main
sniff(filter="tcp", prn=parse)
