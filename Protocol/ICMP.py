from struct import *
from IProtocol import IProtocol

"""
####                       ICMP TRAME                        ####
0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Type      |     Code      |          Checksum             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             unused                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|      Internet Header + 64 bits of Original Data Datagram      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""

class ICMP(IProtocol) :
    PROTOCOL = 1
    BASIC_HEADER_LENGTH = 4
    def unpack(self, packet, tmp_length) :
        ICMP_HEADER_LENGTH = tmp_length + self.BASIC_HEADER_LENGTH
        header = unpack('!BBH' , packet[ICMP_HEADER_LENGTH-self.BASIC_HEADER_LENGTH:ICMP_HEADER_LENGTH])
        self.type = header[0]
        self.code = header[1]
        self.checksum = header[2]
        self.data_length = len(packet) - ICMP_HEADER_LENGTH
        self.data = packet[ICMP_HEADER_LENGTH:]
    def display_info(self) :
        print 'ICMP TRAME'
        print 'Type : ' + str(self.type) + ' Code : ' + str(self.code) + ' Checksum : ' + str(self.checksum)
        #print data.encode('utf8')
        print 'Data : ' + self.data
        print 'Data length : ' + str(self.data_length) + ' ' + str(len(self.data))
