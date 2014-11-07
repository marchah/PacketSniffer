from struct import *
from IProtocol import IProtocol

"""
####          UDP TRAME           ####
0      7 8     15 16    23 24    31  
 +--------+--------+--------+--------+ 
 |     Source      |   Destination   | 
 |      Port       |      Port       | 
 +--------+--------+--------+--------+ 
 |                 |                 | 
 |     Length      |    Checksum     | 
 +--------+--------+--------+--------+ 
 |                                     
 |          data octets ...            
 +---------------- ...
"""

class UDP(IProtocol) :
    PROTOCOL = 17
    BASIC_HEADER_LENGTH = 8
    def unpack(self, packet, tmp_length) :
        UDP_HEADER_LENGTH = tmp_length + UDP.BASIC_HEADER_LENGTH
        header = unpack('!HHHH', packet[UDP_HEADER_LENGTH-UDP.BASIC_HEADER_LENGTH:UDP_HEADER_LENGTH])

        self.source_port = header[0]
        self.destination_port = header[1]
        self.length = header[2]
        self.checksum = header[3]
        self.data_length = len(packet) - UDP_HEADER_LENGTH
        self.data = packet[UDP_HEADER_LENGTH:]
#    def set_data_length(self, data_length) :
#        self.data_length = data_length
#    def set_data(self, data) :
#        self.data = data
    def display_info(self) :
        print 'UDP TRAME'
        print 'Source Port : ' + str(self.source_port) + ' Dest Port : ' + str(self.destination_port)
        print 'Length : ' + str(self.length) + ' Checksum : ' + str(self.checksum)
        #print data.encode('utf8')
        print 'Data : ' + self.data
        print 'Data length : ' + str(self.data_length) + ' ' + str(len(self.data))


