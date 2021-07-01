#Time Trial / RKSYS Tools
import bitstring
import mkwtools_internal.common as common


#I'm not sure what this does, but I assume it relates to Ghosts, so I put it in this file
# ex = 0x045c87 means 2:23.135
class FinishTimeEntry: #3 bytes
    def __init__(self, data=None):
        data = bitstring.BitArray(data)
        self.Minutes = data[0:7].uint
        self.Seconds = data[7:14].uint
        self.Milliseconds = data[14:24].uint
        
class Ghost:
    def __init__(self, data):
        ghost = bytearray(data)
        characterDict = {0:"Mario", 1:"Baby Peach", 2:"Waluigi", 3:"Bowser", 4:"Baby Daisy", 5:"Dry Bones", 6:"Baby Mario", 7:"Luigi", 8:"Toad", 9:"Donkey Kong", 10:"Yoshi", 11:"Wario", 12:"Baby Luigi", 13:"Toadette", 14:"Koopa", 15:"Daisy", 16:"Peach", 17:"Birdo", 18:"Diddy Kong", 19:"King Boo", 20:"Bowser Jr.", 21:"Dry Bowser", 22:"Funky Kong", 23:"Rosalina", 24:"Small Mii A Male", 25:"Small Mii A Female", 26:"Small Mii B Male", 27:"Small Mii B Female", 30:"Medium Mii A Male", 31:"Medium Mii A Female", 32:"Medium Mii B Male", 33:"Medium Mii B Female", 36:"Large Mii A Male", 37:"Large Mii A Female", 38:"Large Mii B Male", 39:"Large Mii B Female"}
        vehicleDict = {0:"Standard Kart S", 1:"Standard Kart M", 2:"Standard Kart L", 3:"Booster Seat", 4:"Classic Dragster", 5:"Offroader", 6:"Mini Beast", 7:"Wild Wing", 8:"Flame Flyer", 9:"Cheep Charger", 10:"Super Blooper", 11:"Piranha Prowler", 12:"Tiny Titan", 13:"Daytripper", 14:"Jetsetter", 15:"Blue Falcon", 16:"Sprinter", 17:"Honeycoupe", 18:"Standard Bike S", 19:"Standard Bike M", 20:"Standard Bike L", 21:"Bullet Bike", 22:"Mach Bike", 23:"Flame Runner", 24:"Bit Bike", 25:"Sugarscoot", 26:"Wario Bike", 27:"Quacker", 28:"Zip Zip", 29:"Shooting Star", 30:"Magikruiser", 31:"Sneakster", 32:"Spear",  33:"Jet Bubble", 34:"Dolphin Dasher", 35:"Phantom"}
        trackDict = {8:'Luigi Circuit', 1:'Moo Moo Meadows', 2:'Mushroom Gorge', 4:"Toad's Factory", 0:'Mario Circuit', 5:'Coconut Mall', 6:'DK Summit', 7:"Wario's Gold Mine", 9:'Daisy Circuit', 15:'Koopa Cape', 11:'Maple Treeway', 3:'Grumble Volcano', 14:'Dry Dry Ruins', 10:'Moonview Highway', 12:"Bowser's Castle", 13:'Rainbow Road', 16:'GCN Peach Beach', 20:'DS Yoshi Falls', 25:'SNES Ghost Valley 2', 26:'N64 Mario Raceway', 27:'N64 Sherbet Land', 31:'GBA Shy Guy Beach', 23:'DS Delfino Square', 18:'GCN Waluigi Stadium', 21:'DS Desert Hills', 30:'GBA Bowser Castle 3', 29:"N64 DK's Jungle Parkway", 17:'GCN Mario Circuit', 24:'SNES Mario Circuit 3', 22:'DS Peach Gardens', 19:'GCN DK Mountain', 28:"N64 Bowser's Castle"}
        controllers = ["Wii Wheel", "Wiimote and Nunchuck", "Classic Controller", "GameCube Controller"]
        driftMap = {True:'Automatic', False:'Manual'}
        if not ghost[0:4].decode('utf8') == 'RKGD':  #Always RKGD
            raise Exception("File is not a Mario Kart Wii Ghost data file.")
        finishingTimeBytes = bitstring.BitArray(ghost[4:7])
        self.finishingTimeMinutes = finishingTimeBytes[0:7].uint
        self.finishingTimeSeconds = finishingTimeBytes[7:14].uint
        self.finishingTimeMilliseconds = finishingTimeBytes[14:24].uint
        if self.finishingTimeMinutes != 0:
            self.prettyFinishingTime = f'{str(self.finishingTimeMinutes)}:{str(self.finishingTimeSeconds).zfill(2)}.{str(self.finishingTimeMilliseconds).zfill(3)}'
        else:
            self.prettyFinishingTime = f'{str(self.finishingTimeSeconds).zfill(2)}.{str(self.finishingTimeMilliseconds).zfill(3)}'
        self.trackId = bitstring.BitArray(ghost[7:8])[0:6].uint
        self.track = trackDict.get(self.trackId)
        metadata = bitstring.BitArray(ghost[8:15])
        self.vehicleId = metadata[0:6].uint
        self.vehicle = vehicleDict.get(self.vehicleId)
        self.characterId = metadata[6:12].uint
        self.character = characterDict.get(self.characterId)
        self.year = 2000 + metadata[12:19].uint
        self.month = metadata[19:23].uint
        self.day = metadata[23:28].uint
        self.prettyDate = f'{self.year}/{self.month}/{self.day}'
        self.controllerId = metadata[28:32].uint
        self.controller = controllers[self.controllerId]
        self.isCompressed = metadata[37]
        self.ghostType = hex(metadata[40:46].uint)
        self.driftType = driftMap[metadata[48]]
        self.countryId = int.from_bytes(ghost[52:53], 'big')
        self.countryCode = common.countryCodeFromId(self.countryId)
        miiNamePre = ghost[62:82].decode(u"utf-16be")
        self.miiName, _, _ = miiNamePre.partition('\x00')
        self.miiData = ghost[60:134]