from struct import *
from IProtocol import IProtocol

"""
####                      ARP HEADER                         ####
0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Hardware Type         |         Protocol Type         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|H. Addr. Length|P. Addr. Length|             Opcode            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                     Source Hardware Address                   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                     Source Protocol Address                   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Hardware Address               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Protocol Address               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""

class ARP(IProtocol) :
    PROTOCOL = IProtocol.CONVERT_ETHERNET_TYPE('0x0806')
    BASIC_HEADER_LENGTH = 11
    def unpack(self, packet, ethernet_header_length) :
        ARP_HEADER_LENGTH = ethernet_header_length + ARP.BASIC_HEADER_LENGTH
        header = unpack('!HHBH4s', packet[ethernet_header_length: ARP_HEADER_LENGTH])
        self.hardware_type = header[0]
        self.protocol_type = header[1]
        self.hardware_address_length = header[2] >> 4
        self.protocol_address_length = header[2] & 0xF
        self.opcode = header[3]
        self.source_hardware_address = header[4]
    def display_info(self) :
        print 'Protocol ARP'
        print 'Hardware Type: ' + str(self.hardware_type) + ', Protocol Type: ' + str(self.protocol_type)
        print 'Hardware Address Length: ' + str(self.hardware_address_length) + ', Protocol Address Length: ' + str(self.protocol_address_length) + ', Opcode: ' + str(self.opcode)
        print 'Source Hardware Address: ' + self.source_hardware_address
