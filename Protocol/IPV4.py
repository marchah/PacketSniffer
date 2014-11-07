import socket
from struct import *
from IProtocol import IProtocol

from Protocol.TCP import TCP
from Protocol.UDP import UDP
from Protocol.ICMP import ICMP

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

class IPV4(IProtocol) :
    PROTOCOL = IProtocol.CONVERT_ETHERNET_TYPE('0x0800')
    BASIC_HEADER_LENGTH = 20
    def unpack(self, packet, ethernet_header_length) :
        IP_HEADER_LENGTH = ethernet_header_length + IPV4.BASIC_HEADER_LENGTH
        header = unpack('!BBHHHBBH4s4s', packet[ethernet_header_length: IP_HEADER_LENGTH])
        tmp = header[0]
        self.version = tmp >> 4
        self.ihl = tmp & 0xF
        self.header_length = self.ihl * 4
        self.ttl = header[5]
        self.protocol = header[6]
        self.s_addr = socket.inet_ntoa(header[8])
        self.d_addr = socket.inet_ntoa(header[9])
        self._set_protocol(packet, ethernet_header_length + self.header_length)
    def _set_protocol(self, packet, ip_header_length) :
        if self.protocol == TCP.PROTOCOL :        
            tcp = TCP()
            tcp.unpack(packet, ip_header_length)
            tcp.display_info()
        elif self.protocol == UDP.PROTOCOL :            
            upd = UDP()
            upd.unpack(packet, ip_header_length)
            upd.display_info()
        elif self.protocol == ICMP.PROTOCOL :
            icmp = ICMP()
            icmp.unpack(packet, ip_header_length)
            icmp.display_info()
#some other IP packet like IGMP
        else :
            print 'Protocol other than TCP/UDP/ICMP'
    def display_info(self) :
        print 'Protocol IPV4'
        print 'Version: ' + str(self.version) + ', IHL: ' + str(self.ihl) + ', Total Length: ' + str(self.header_length)
        print 'Time to Live: ' + str(self.ttl) + ', Protocol: ' + str(self.protocol)
        print 'Source Address : ' + str(self.s_addr)
        print 'Destination Address : ' + str(self.d_addr)
