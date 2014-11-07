import socket, sys
from struct import *

from Protocol.IPV4 import IPV4
from Protocol.ARP import ARP

#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b

def convert_to_little_endian (a) :
  return a[0]+a[1]+a[4]+a[5]+a[2]+a[3]

def convert_ether_type (a) :
  return int(convert_to_little_endian(a), 16)

PROTOCOL_IPV4 = convert_ether_type('0x0800')
PROTOCOL_ARP = convert_ether_type('0x0806')

try:
    s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error , msg:
    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
while True:
    rawPacket = s.recvfrom(65565)
     
    packet = rawPacket[0]

    addressPacket = rawPacket[1]
    print addressPacket

    """
        ####                    ETHERNET HEADER                      ####
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |       Ethernet destination address (first 32 bits)            |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | Ethernet dest (last 16 bits)  |Ethernet source (first 16 bits)|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |       Ethernet source address (last 32 bits)                  |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |        Type code              |                               |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """
    ETH_HEADER_LENGTH = 6+6+2
    eth_header = packet[:ETH_HEADER_LENGTH]
    eth = unpack('!6s6sH', eth_header);
    addrMacDestination = eth_addr(eth[0])
    addrMacSource = eth_addr(eth[1])
    eth_protocol = socket.ntohs(eth[2])
    print 'Destination MAC : ' + addrMacDestination + ' Source MAC : ' + addrMacSource + ' Protocol : ' + str(eth_protocol)
    
    if eth_protocol == IPV4.PROTOCOL :
      ipv4 = IPV4()
      ipv4.unpack(packet, ETH_HEADER_LENGTH)
      ipv4.display_info()
      print ''
    elif eth_protocol == ARP.PROTOCOL :
      arp = ARP()
      arp.unpack(packet, ETH_HEADER_LENGTH)
      arp.display_info()
    else :
      print ARP.PROTOCOL
      print 'Not Protocol IP or ARP: ' + str(eth_protocol)

    print
