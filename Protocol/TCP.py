from struct import *
from IProtocol import IProtocol

"""
####                        TCP TRAME                        ####
0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |           |U|A|P|R|S|F|                               |
| Offset| Reserved  |R|C|S|S|Y|I|            Window             |
|       |           |G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""

class TCP(IProtocol) :
    PROTOCOL = 6
    BASIC_HEADER_LENGTH = 20
    def unpack(self, packet, tmp_length) :
        TCP_HEADER_LENGTH = tmp_length + TCP.BASIC_HEADER_LENGTH
        header = unpack('!HHLLBBHHH', packet[TCP_HEADER_LENGTH-TCP.BASIC_HEADER_LENGTH:TCP_HEADER_LENGTH])
        self.source_port = header[0]
        self.destination_port = header[1]
        self.sequence = header[2]
        self.acknowledgment = header[3]
        self.data_offset_reserved = header[4]
        self.header_length = self.data_offset_reserved >> 4
        self.window = header[5]
        self.checksum = header[6]
        self.urgent_pointer = header[7]
        self.options = header[8]
        self.headers_length = tmp_length + (self.header_length * 4)
        self.data_length = len(packet) - self.headers_length
        self.data = packet[self.data_length:]
    def display_info(self) :
        print 'TCP TRAME'
        print 'Source Port : ' + str(self.source_port) + ' Dest Port : ' + str(self.destination_port)
        print 'Sequence Number : ' + str(self.sequence)
        print 'Acknowledgement : ' + str(self.acknowledgment)
        print 'Data Offset Reserved : ' + str(self.data_offset_reserved) + ' Window : ' + str(self.window)
        print 'Checksum : ' + str(self.checksum) + ' Urgent Pointer : ' + str(self.urgent_pointer)
        print 'Options : ' + str(self.options)
        #print data.encode('utf8')
        print 'Data : ' + self.data
        print 'Data length : ' + str(self.data_length) + ' ' + str(len(self.data))
