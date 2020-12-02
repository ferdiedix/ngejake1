#!/usr/bin/python3
# -*- coding: utf-8 -*-

#BetCalculator_999dice
#bancetz.Laut_
import sys

ij = '\033[92m'
rd = '\033[91m'
rs = '\033[0;0m'
sekat = f"{rs}|"

x = 0
totbet = 0
b = float(input("Balance: "))
bb = float(input("Base Bet: "))
al = float(input("If Lose: "))

while True:
    x+=1
    totbet += bb
    b -= bb
    if bb <= b:
        print(f"{x}. {sekat} {rd}-{bb:.8f} {sekat} {rd}-{totbet:.8f} {sekat} {ij}{b:.8f}{rs}")
        bb = bb * al
    else:
        print(f"{x}. {sekat} {rd}-{bb:.8f} {sekat} {rd}-{totbet:.8f} {sekat} {ij}{b:.8f}{rs}")
        sys.exit()
