class IProtocol(object):
    PROTOCOL = -1
    BASIC_HEADER_LENGTH = -1
    def unpack(self, packet, tmp_length):
        raise NotImplementedError( "Should have implemented this" )
    def display_info(self):
        raise NotImplementedError( "Should have implemented this" )
