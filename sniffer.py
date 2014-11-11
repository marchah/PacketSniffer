from select import select
import socket
import sys

from impacket.ImpactDecoder import EthDecoder
from impacket.ImpactPacket import IP, TCP, UDP, ICMP, Ethernet, ARP

import fcntl
import struct
import array

def all_interfaces():
	max_possible = 128 # arbitrary. raise if needed.
	bytes = max_possible * 32
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	names = array.array('B', '\0' * bytes)
	outbytes = struct.unpack('iL', fcntl.ioctl(
			s.fileno(),
			0x8912, # SIOCGIFCONF
			struct.pack('iL', bytes, names.buffer_info()[0])
			))[0]
	namestr = names.tostring()
	lst = []
	for i in range(0, outbytes, 40):
		name = namestr[i:i+16].split('\0', 1)[0]
		ip = namestr[i+20:i+24]
		lst.append((name, ip))
	return lst
	
def format_ip(addr):
	return str(ord(addr[0])) + '.' + \
	    str(ord(addr[1])) + '.' + \
	    str(ord(addr[2])) + '.' + \
	    str(ord(addr[3]))
 
 
ifs = all_interfaces()
DEFAULT_INTERFACES = []
if len(ifs) == 0 :
	print "You don't have the right to listen on any interface."
	sys.exit(0)
for i in ifs:
	DEFAULT_INTERFACES.append(i[0])
	print "%12s %s" % (i[0], format_ip(i[1]))

if len(sys.argv) == 1:
        toListen = []
        print "Listening on all interface available."
else:
        toListen = sys.argv[1:]

sockets = []
listening = []
if len(toListen) == 0:
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
	sockets.append(s)
	print "Listening on interfaces:", DEFAULT_INTERFACES
else:
	for interface in toListen:
		try:
			print interface
			s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
			s.bind((interface, 0x0800))
			sockets.append(s)
			listening.append(interface)
		except socket.error:
			print "Ignoring unknown interface:", interface
			continue
	if len(toListen) == 0:
		print "There are no interfaces available."
		sys.exit(0)
	print "Listening on interfaces:", listening

decoder = EthDecoder()
while len(sockets) > 0:
    ready = select(sockets, [], [])[0]
    for s in ready:
        packet = s.recvfrom(4096)[0]
        if 0 == len(packet):
		sockets.remove(s)
		s.close()
        else:
	    l1 = decoder.decode(packet)
            if isinstance(l1, Ethernet):
                print 'Eth',
                l2 = l1.child()
                if isinstance(l2,IP):
                    print "IP",
                    l3=l2.child()
                    if isinstance(l3,TCP):
                        print "TCP"
                    elif isinstance(l3,UDP):
                        print "UDP"
                    elif isinstance(l3,ICMP):
                        print "IMCP"
                    else :
                        print "No TCP or UDP or ICMP"
		elif isinstance(l2,ARP):
			print "ARP"
                else :
                    print "No IP or ARP"
            else :
                print 'No Eth'
