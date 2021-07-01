'''
Created on Jul 1, 2021

@author: willg
'''

#This module is an example how one might use the mkwtools library

import mkwtools
FC = '4086-2278-0250'
badwolf_wiimmfi_mii_object = mkwtools.get_wiimmfi_mii(FC)

print("Bad Wolf Mii Gender:", badwolf_wiimmfi_mii_object.gender)
print("Bad Wolf Mii Name:", badwolf_wiimmfi_mii_object.miiName)
print("Bad Wolf Country Code:", badwolf_wiimmfi_mii_object.countryCode)

