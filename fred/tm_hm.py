#!/usr/bin/env python3

TM_OFFSET   = 0x45A80C
TM_VAL_SIZE = 2
TM_TBL_SIZE = 50 * TM_VAL_SIZE
HM_OFFSET = TM_TBL_SIZE + TM_OFFSET

# Lift from
# https://bulbapedia.bulbagarden.net/wiki/TM#List_of_TMs
TM_TABLE_ORIGINAL = "0801510160015b012e005c00020153014b01ed00\
                     f1000d013a003b003f007100b600f000ca00db00\
                     da004c00e700550057005900d8005b005e00f700\
                     1801680073005f013500bc00c9007e003d014c01\
                     0301070122019c00d500a800d3001d0121013b01"

# All 8 of the HMs (including Dive, which can't be used in Fire)
HM_TABLE_ORIGINAL = "0f001300390046009400f9007f00"
