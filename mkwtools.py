#MKW Python Tools by Will
#these are just a random collection of functions and other things that I thought would be useful for anyone looking to code tools for MKW in python or similar.

import requests
import binascii
import hashlib
import base64
import struct
import bitstring


#DWC Tools

def fc_to_pid(pid, gameid):
    name = bytes([
        (pid >>  0) & 0xFF,
        (pid >>  8) & 0xFF,
        (pid >> 16) & 0xFF,
        (pid >> 24) & 0xFF,
        int(gameid[3]),
        int(gameid[2]),
        int(gameid[1]),
        int(gameid[0])])
    return pid & 0xFFFFFFFF

def pid_to_fc(pid, gameid):
    name = bytes([
        (pid >>  0) & 0xFF,
        (pid >>  8) & 0xFF,
        (pid >> 16) & 0xFF,
        (pid >> 24) & 0xFF,
        int(gameid[3]),
        int(gameid[2]),
        int(gameid[1]),
        int(gameid[0])])
    hash_ = int(hashlib.md5(name).hexdigest()[:2], 16) >> 1
    return (hash_ << 32) | (pid & 0xFFFFFFFF)

class SakeMiiResponse:
	def __init__(self, responseObject, responseContent):
		fullWiimmfiResponse = bytearray(base64.b64decode(str(responseContent)[399:527]))
		self.miiBytes = bytes(fullWiimmfiResponse[0:74])
		self.miiCRC16 = bytes(fullWiimmfiResponse[74:76])
		self.unknown1 = bytes(fullWiimmfiResponse[76]) #set to null
		self.unknown2 = binascii.hexlify(fullWiimmfiResponse[77:84])
		self.gameId = fullWiimmfiResponse[84:88].decode('utf8')
		self.countryCode = int.from_bytes(fullWiimmfiResponse[88:89], 'big')
		self.regionCode = int.from_bytes(fullWiimmfiResponse[89:90], 'big')
		self.unknown3 = bytes(fullWiimmfiResponse[90:92])
		self.playerLatitude = int.from_bytes(bytes(fullWiimmfiResponse[92:94]), 'big', signed=True)
		self.playerLongitude = int.from_bytes(bytes(fullWiimmfiResponse[94:96]), 'big', signed=True) 
		self.statusCode = responseObject.status_code
		self.headers = responseObject.headers

countryDict = {
1:'JP',
2:'AQ',
3:'NL',
4:'FK',
5:'GB',
6:'GB',
7:'SX',
8:'AI',
9:'AG',
10:'AR',
11:'AW',
12:'BS',
13:'BB',
14:'BZ',
15:'BO',
16:'BR',
17:'VG',
18:'CA',
19:'KY',
20:'CL',
21:'CO',
22:'CR',
23:'DM',
24:'DO',
25:'EC',
26:'SV',
27:'GF',
28:'GD',
29:'GP',
30:'GT',
31:'GY',
32:'HT',
33:'HN',
34:'JM',
35:'MQ',
36:'MX',
37:'MS',
38:'AN',
39:'NI',
40:'PA',
41:'PY',
42:'PE',
43:'KN',
44:'LC',
45:'VC',
46:'SR',
47:'TT',
48:'TC',
49:'US',
50:'UY',
51:'VI',
52:'VE',
53:'AM',
54:'BY',
55:'GE',
56:'XK',
57:'AK',
58:'AH',
59:'NY',
62:'AX',
63:'FO',
64:'AL',
65:'AU',
66:'AT',
67:'BE',
68:'BA',
69:'BW',
70:'BG',
71:'HR',
72:'CY',
73:'CZ',
74:'DK',
75:'EE',
76:'FI',
77:'FR',
78:'DE',
79:'GR',
80:'HU',
81:'IS',
82:'IE',
83:'IT',
84:'LV',
85:'LS',
86:'LI',
87:'LT',
88:'LU',
89:'MK',
90:'MT',
91:'ME',
92:'MZ',
93:'NA',
94:'NL',
95:'NZ',
96:'NO',
97:'PL',
98:'PT',
99:'RO',
100:'RU',
101:'RS',
102:'SK',
103:'SI',
104:'ZA',
105:'ES',
106:'SZ',
107:'SE',
108:'CH',
109:'TR',
110:'GB',
111:'ZM',
112:'ZW',
113:'AZ',
114:'MR',
115:'ML',
116:'NE',
117:'TD',
118:'SD',
119:'ER',
120:'DJ',
121:'SO',
122:'AD',
123:'GI',
124:'GG',
125:'IM',
126:'JE',
127:'MC',
128:'TW',
129:'KH',
130:'LA',
131:'MN',
132:'MM',
133:'NP',
134:'VN',
135:'KP',
136:'KR',
137:'BD',
138:'BT',
139:'BN',
140:'MV',
141:'LK',
142:'TL',
143:'IO',
144:'HK',
145:'MO',
146:'CK',
147:'NU',
148:'NF',
149:'MP',
150:'AS',
151:'GU',
152:'ID',
153:'SG',
154:'TH',
155:'PH',
156:'MY',
157:'BL',
158:'MF',
159:'PM',
160:'CN',
161:'AF',
162:'KZ',
163:'KG',
164:'PK',
165:'TJ',
166:'TM',
167:'UZ',
168:'AE',
169:'IN',
170:'EG',
171:'OM',
172:'QA',
173:'KW',
174:'SA',
175:'SY',
176:'BH',
177:'JO',
178:'IR',
179:'IQ',
180:'IL',
181:'LB',
182:'PS',
183:'YE',
184:'SM',
185:'VS',
186:'BM',
187:'PF',
188:'RE',
189:'YT',
190:'NC',
191:'WF',
192:'NG',
193:'AO',
194:'GH',
195:'TG',
196:'BJ',
197:'BF',
198:'CI',
199:'LR',
200:'SL',
201:'GN',
202:'GW',
203:'SN',
204:'GM',
205:'CV',
206:'SH',
207:'MD',
208:'UA',
209:'CM',
211:'CD',
212:'CG',
213:'GQ',
214:'GA',
215:'ST',
216:'DZ',
217:'ET',
218:'LY',
219:'MA',
220:'SS',
221:'TN',
222:'EH',
223:'CU',
224:'BI',
225:'KM',
226:'KE',
227:'MG',
228:'MW',
229:'MU',
230:'RW',
231:'SC',
232:'TZ',
233:'UG',
234:'FR',
235:'PN',
236:'GB',
237:'GS',
238:'FM',
239:'FJ',
240:'KI',
241:'MH',
242:'NR',
243:'PW',
244:'PG',
245:'WS',
246:'SB',
247:'TK',
248:'TO',
249:'TV',
250:'VU',
251:'CX',
252:'CC',
253:'PR',
254:'GL'}

def countryCodeFromId(countryId: int):
	return countryDict.get(countryId, None)

#pid or fc
def get_wiimmfi_mii(playerid: str):
	playerid = fc_to_pid(int(playerid.replace("-","")), b'RMCJ')
	wiimmfi_sake = 'http://mariokartwii.sake.gs.wiimmfi.de/SakeStorageServer/StorageServer.asmx'
	mii_data = requests.post(wiimmfi_sake, data=f'<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns1="http://gamespy.net/sake"><SOAP-ENV:Body><ns1:SearchForRecords><ns1:gameid>1687</ns1:gameid><ns1:secretKey>test</ns1:secretKey><ns1:loginTicket>23c715d620f986c22Pwwii</ns1:loginTicket><ns1:tableid>FriendInfo</ns1:tableid><ns1:filter>ownerid&#x20;=&#x20;{playerid}</ns1:filter><ns1:sort>recordid</ns1:sort><ns1:offset>0</ns1:offset><ns1:max>1</ns1:max><ns1:surrounding>0</ns1:surrounding><ns1:ownerids></ns1:ownerids><ns1:cacheFlag>0</ns1:cacheFlag><ns1:fields><ns1:string>info</ns1:string></ns1:fields></ns1:SearchForRecords></SOAP-ENV:Body></SOAP-ENV:Envelope>')
	return SakeMiiResponse(mii_data, mii_data.content)

#General Tools

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


#Time Trial / RKSYS Tools


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
		self.countryCode = countryCodeFromId(self.countryId)
		miiNamePre = ghost[62:82].decode(u"utf-16be")
		self.miiName, _, _ = miiNamePre.partition('\x00')
		self.miiData = ghost[60:134]
