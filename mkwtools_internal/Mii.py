import binascii
import bitstring


class Mii:
    def __init__(self, data):
        data = bytearray(data)
        bits = bitstring.BitArray(data)
        genderMap = {False:"Male", True:"Female"}
        colorMap = {0:'Red', 1:'Orange', 2:'Yellow', 3:'Light Green', 4:'Dark Green', 5:'Dark Blue', 6:'Light Blue', 7:'Pink', 8:'Purple', 9:'Brown', 10:'White', 11:'Black'}
        self.gender = genderMap[bits[1]]
        if bits[2:6].uint == 0:
            self.birthdaySet = False
            self.birthMonth = None
            self.birthDay = None
        else:
            self.birthdaySet = True
            self.birthMonth = bits[2:6].uint
            self.birthDay = bits[6:11].uint
        self.shirtColor = colorMap[bits[11:15].uint]
        self.isFavorite = bits[16]
        self.miiName = data[2:16].decode(u"utf-16be").strip('\x00')
        self.bodyHeight = data[16:17]
        self.bodyWeight = data[17:18]
        self.avatarId = binascii.hexlify(data[24:28])
        self.clientId = binascii.hexlify(data[28:32])
        self.faceType = bits[256:259].uint
        self.faceColor = bits[259:262].uint
        self.facialFeature = bits[262:266].uint
        self.unknown1 = bits[266:269].uint
        self.doesMingle = bits[270]
        self.unknown2 = bits[271]
        self.downloaded = bits[272]
        self.hairType = bits[272:279].uint
        self.hairColor = bits[279:282].uint
        #self.

