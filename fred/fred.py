#!/usr/bin/env python3

from .moves import *
from .tm_hm import *

# TM TODO
# TODO figure out how to edit the text for the TMs
# TODO figure out how to edit pokemon that can learn the TM
# TODO Inspect TM table and report on modifications

# Only used for testing
def main():
    with open( 'exclude/Pokemon_Fire.rom', 'rb' ) as fh:
        fh.seek(HM_OFFSET)
        print( fh.read(14).hex() )
        fh.seek(TM_OFFSET)
        print("TM")
        for i in range(50):
            val = fh.read(2).hex()
            string = val[2:] + val[:2]
            print(string + " " + str(i+1))
        print("HM")
        for i in range(7):
            val = fh.read(2).hex()
            string = val[2:] + val[:2]
            print(string + " " + str(i+1))

def current_TM_table( fh ):
    pass

def current_HM_table( fh ):
    pass

def set_HM( fh, hm_numb, move_index ):
    pass

def set_TM( fh, tm_numb, move_index ):
    pass

def is_TM_table_original( fh ):
    fh.seek(TM_OFFSET)
    if fh.read(TM_TBL_SIZE).hex() == TM_TABLE_ORIGINAL:
        return True
    return False

def is_HM_table_original( fh ):
    fh.seek(HM_OFFSET)
    if fh.read(HM_TBL_SIZE).hex() == HM_TABLE_ORIGINAL:
        return True
    return False

def restore_HM_table( fh ):
    fh.seek(HM_OFFSET)
    for b in [HM_TABLE_ORIGINAL[i:i+2] for i in range(0, len(HM_TABLE_ORIGINAL), 2)]:
        fh.write(bytes.fromhex(b), byteorder='big')

def restore_TM_table( fh ):
    fh.seek(TM_OFFSET)
    for b in [TM_TABLE_ORIGINAL[i:i+2] for i in range(0, len(TM_TABLE_ORIGINAL), 2)]:
        fh.write(bytes.fromhex(b), byteorder='big')

def move_from_index( index )
    return MOVE_INDEX[index+1]

if __name__ == "__main__":
    main()
