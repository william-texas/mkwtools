#MKW Python Tools by Will
#these are just a random collection of functions and other things that I thought would be useful for anyone looking to code tools for MKW in python or similar.


#This is the base package that people will interface with
from mkwtools_internal.WiimmfiMii import get_wiimmfi_mii, WiimmfiMii
from mkwtools_internal.common import *
from mkwtools_internal.Ghost import Ghost #, FinishTimeEntry too? I am unclear if this is privately used for Ghosts and be abstracted away or if it should be part of the public interface
from mkwtools_internal.Mii import Mii

if __name__ == '__init__':
    print("Running test cases:")
    #Run test cases here
    

