import socket, sys
from struct import *

from Protocol.TCP import TCP
from Protocol.UDP import UDP
from Protocol.ICMP import ICMP

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


PROTOCOL_TCP = 6
PROTOCOL_UDP = 17
PROTOCOL_ICMP = 1

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
    
    if eth_protocol == PROTOCOL_IPV4 :
        """
        ####                       IP HEADER                         ####
        0                   1                   2                   3
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |Version|  IHL  |Type of Service|          Total Length         |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |         Identification        |Flags|      Fragment Offset    |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |  Time to Live |    Protocol   |         Header Checksum       |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |                       Source Address                          |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |                    Destination Address                        |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |                    Options                    |    Padding    |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        """

        IP_HEADER_LENGTH = ETH_HEADER_LENGTH + 20
        ip_header = unpack('!BBHHHBBH4s4s', packet[ETH_HEADER_LENGTH: IP_HEADER_LENGTH])
        tmp = ip_header[0]
        version = tmp >> 4
        ihl = tmp & 0xF

        iph_length = ihl * 4
        
        ttl = ip_header[5]
        protocol = ip_header[6]
        s_addr = socket.inet_ntoa(ip_header[8]);
        d_addr = socket.inet_ntoa(ip_header[9]);
        print ip_header
        print 'Version: ' + str(version) + ', IHL: ' + str(ihl) + ', IP Header Length: ' + str(iph_length) + ', Time to Live: ' + str(ttl) + ', Protocol: ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
        if protocol == TCP.PROTOCOL :

          tcp = TCP()
          tcp.unpack(packet, ETH_HEADER_LENGTH + iph_length)
          tcp.display_info()

        elif protocol == UDP.PROTOCOL :

          upd = UDP()
          upd.unpack(packet, ETH_HEADER_LENGTH + iph_length)
          upd.display_info()

        elif protocol == ICMP.PROTOCOL :

          icmp = ICMP()
          icmp.unpack(packet, ETH_HEADER_LENGTH + iph_length)
          icmp.display_info()

#some other IP packet like IGMP
        else :
          print 'Protocol other than TCP/UDP/ICMP'
    elif eth_protocol == PROTOCOL_ARP :
      print 'Protocol ARP'
    else :
        print 'Not Protocol IP: ' + str(eth_protocol)

    print
