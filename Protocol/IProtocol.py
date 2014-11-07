class IProtocol(object):
    PROTOCOL = -1
    BASIC_HEADER_LENGTH = -1
    @staticmethod
    def CONVERT_TO_LITTLE_ENDIAN(a) :
        return a[0]+a[1]+a[4]+a[5]+a[2]+a[3]
    @staticmethod
    def CONVERT_ETHERNET_TYPE(a) :
        return int(IProtocol.CONVERT_TO_LITTLE_ENDIAN(a), 16)
    def unpack(self, packet, tmp_length):
        raise NotImplementedError( "Should have implemented this" )
    def display_info(self):
        raise NotImplementedError( "Should have implemented this" )
