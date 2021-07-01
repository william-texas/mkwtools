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
		miiName = data[2:22].decode(u"utf-16be").strip('\x00')
		self.miiName, _, _ = miiName.partition('\x00')
		self.bodyHeight = int.from_bytes(data[22:23], 'big')
		self.bodyWeight = int.from_bytes(data[23:24], 'big')
		self.avatarId = binascii.hexlify(data[24:28])
		self.clientId = binascii.hexlify(data[28:32])
		self.faceType = bits[256:259].uint
		self.faceColor = bits[259:262].uint
		self.facialFeature = bits[262:266].uint
		self.unknown1 = bits[266:269].uint
		self.doesMingle = bits[269]
		self.unknown2 = bits[270]
		self.downloaded = bits[271]
		self.hairType = bits[272:279].uint
		self.hairColor = bits[279:282].uint
		self.hairFlipped = bits[282]
		self.unknown3 = bits[283:288].uint
		self.eyebrowType = bits[288:293].uint
		self.unknown4 = bits[293]
		self.eyebrowRotation = bits[294:298].uint
		self.unknown5 = bits[298:304].uint
		self.eyebrowColor = bits[304:307].uint
		self.eyebrowSize = bits[307:311].uint
		self.eyebrowVertical = bits[311:316].uint
		self.eyebrowHorizontal = bits[316:320].uint
		self.eyeType = bits[320:326].uint
		self.unknown6 = bits[326:328].uint
		self.eyeRotation = bits[328:331].uint
		self.eyeVertical = bits[331:336].uint
		self.eyeColor = bits[336:339].uint
		self.unknown7 = bits[339]
		self.eyeSize = bits[340:343].uint
		self.eyeHorizontal = bits[343:347].uint
		self.unknown8 = bits[347:352].uint
		self.noseType = bits[352:356].uint
		self.noseSize = bits[356:360].uint
		self.noseVertical = bits[360:365].uint
		self.unknown9 = bits[365:368].uint
		self.mouthType = bits[368:373].uint
		self.mouthColor = bits[373:375].uint
		self.mouthSize = bits[375:379].uint
		self.mouthVertical = bits[379:384].uint
		self.glassesType = bits[384:388].uint
		self.glassesColor = bits[388:391].uint
		self.unknown10 = bits[391]
		self.glassesSize = bits[392:395].uint
		self.glassesVertical = bits[395:400].uint
		self.facialHairMustache = bits[400:402].uint
		self.facialHairBeard = bits[402:404].uint
		self.facialHairColor = bits[404:407].uint
		self.facialHairSize = bits[407:411].uint
		self.hasMole = bits[411]
		self.moleSize = bits[412:416].uint
		self.moleVertical = bits[416:421].uint
		self.moleHorizontal = bits[421:426].uint
		self.unknown11 = bits[426]
		creatorName = data[54:74].decode(u"utf-16be").strip('\x00')
		self.creatorName, _, _ = creatorName.partition('\x00')
