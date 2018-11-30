from rdpy.pdu.base_pdu import PDU


class BitmapUpdateData(PDU):
    """
    https://msdn.microsoft.com/en-us/library/cc240612.aspx
    """

    def __init__(self, destLeft: int, destTop: int, destRight: int, destBottom: int, width: int, heigth: int,
                 bitsPerPixel: int, flags: int, bitmapData: bytes):
        super().__init__()
        self.destLeft = destLeft
        self.destTop = destTop
        self.destRight = destRight
        self.destBottom = destBottom
        self.width = width
        self.heigth = heigth
        self.bitsPerPixel = bitsPerPixel
        self.flags = flags
        self.bitmapData = bitmapData