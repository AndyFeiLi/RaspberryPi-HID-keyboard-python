#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

NULL_CHAR = chr(0)

keyboard = {}

keyboard["a"] = NULL_CHAR*2+chr(4)+NULL_CHAR*5
keyboard["b"] = NULL_CHAR*2+chr(5)+NULL_CHAR*5
keyboard["c"] = NULL_CHAR*2+chr(6)+NULL_CHAR*5
keyboard["d"] = NULL_CHAR*2+chr(7)+NULL_CHAR*5
keyboard["e"] = NULL_CHAR*2+chr(8)+NULL_CHAR*5
keyboard["f"] = NULL_CHAR*2+chr(9)+NULL_CHAR*5
keyboard["g"] = NULL_CHAR*2+chr(10)+NULL_CHAR*5
keyboard["h"] = NULL_CHAR*2+chr(11)+NULL_CHAR*5
keyboard["i"] = NULL_CHAR*2+chr(12)+NULL_CHAR*5
keyboard["j"] = NULL_CHAR*2+chr(13)+NULL_CHAR*5
keyboard["k"] = NULL_CHAR*2+chr(14)+NULL_CHAR*5
keyboard["l"] = NULL_CHAR*2+chr(15)+NULL_CHAR*5
keyboard["m"] = NULL_CHAR*2+chr(16)+NULL_CHAR*5
keyboard["n"] = NULL_CHAR*2+chr(17)+NULL_CHAR*5
keyboard["o"] = NULL_CHAR*2+chr(18)+NULL_CHAR*5
keyboard["p"] = NULL_CHAR*2+chr(19)+NULL_CHAR*5
keyboard["q"] = NULL_CHAR*2+chr(20)+NULL_CHAR*5
keyboard["r"] = NULL_CHAR*2+chr(21)+NULL_CHAR*5
keyboard["s"] = NULL_CHAR*2+chr(22)+NULL_CHAR*5
keyboard["t"] = NULL_CHAR*2+chr(23)+NULL_CHAR*5
keyboard["u"] = NULL_CHAR*2+chr(24)+NULL_CHAR*5
keyboard["v"] = NULL_CHAR*2+chr(25)+NULL_CHAR*5
keyboard["w"] = NULL_CHAR*2+chr(26)+NULL_CHAR*5
keyboard["x"] = NULL_CHAR*2+chr(27)+NULL_CHAR*5
keyboard["y"] = NULL_CHAR*2+chr(28)+NULL_CHAR*5
keyboard["z"] = NULL_CHAR*2+chr(29)+NULL_CHAR*5

keyboard["A"] = chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5
keyboard["B"] = chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5
keyboard["C"] = chr(32)+NULL_CHAR+chr(6)+NULL_CHAR*5
keyboard["D"] = chr(32)+NULL_CHAR+chr(7)+NULL_CHAR*5
keyboard["E"] = chr(32)+NULL_CHAR+chr(8)+NULL_CHAR*5
keyboard["F"] = chr(32)+NULL_CHAR+chr(9)+NULL_CHAR*5
keyboard["G"] = chr(32)+NULL_CHAR+chr(10)+NULL_CHAR*5
keyboard["H"] = chr(32)+NULL_CHAR+chr(11)+NULL_CHAR*5
keyboard["I"] = chr(32)+NULL_CHAR+chr(12)+NULL_CHAR*5
keyboard["J"] = chr(32)+NULL_CHAR+chr(13)+NULL_CHAR*5
keyboard["K"] = chr(32)+NULL_CHAR+chr(14)+NULL_CHAR*5
keyboard["L"] = chr(32)+NULL_CHAR+chr(15)+NULL_CHAR*5
keyboard["M"] = chr(32)+NULL_CHAR+chr(16)+NULL_CHAR*5
keyboard["N"] = chr(32)+NULL_CHAR+chr(17)+NULL_CHAR*5
keyboard["O"] = chr(32)+NULL_CHAR+chr(18)+NULL_CHAR*5
keyboard["P"] = chr(32)+NULL_CHAR+chr(19)+NULL_CHAR*5
keyboard["Q"] = chr(32)+NULL_CHAR+chr(20)+NULL_CHAR*5
keyboard["R"] = chr(32)+NULL_CHAR+chr(21)+NULL_CHAR*5
keyboard["S"] = chr(32)+NULL_CHAR+chr(22)+NULL_CHAR*5
keyboard["T"] = chr(32)+NULL_CHAR+chr(23)+NULL_CHAR*5
keyboard["U"] = chr(32)+NULL_CHAR+chr(24)+NULL_CHAR*5
keyboard["V"] = chr(32)+NULL_CHAR+chr(25)+NULL_CHAR*5
keyboard["W"] = chr(32)+NULL_CHAR+chr(26)+NULL_CHAR*5
keyboard["X"] = chr(32)+NULL_CHAR+chr(27)+NULL_CHAR*5
keyboard["Y"] = chr(32)+NULL_CHAR+chr(28)+NULL_CHAR*5
keyboard["Z"] = chr(32)+NULL_CHAR+chr(29)+NULL_CHAR*5

keyboard["1"] = NULL_CHAR*2+chr(30)+NULL_CHAR*5
keyboard["2"] = NULL_CHAR*2+chr(31)+NULL_CHAR*5
keyboard["3"] = NULL_CHAR*2+chr(32)+NULL_CHAR*5
keyboard["4"] = NULL_CHAR*2+chr(33)+NULL_CHAR*5
keyboard["5"] = NULL_CHAR*2+chr(34)+NULL_CHAR*5
keyboard["6"] = NULL_CHAR*2+chr(35)+NULL_CHAR*5
keyboard["7"] = NULL_CHAR*2+chr(36)+NULL_CHAR*5
keyboard["8"] = NULL_CHAR*2+chr(37)+NULL_CHAR*5
keyboard["9"] = NULL_CHAR*2+chr(38)+NULL_CHAR*5
keyboard["0"] = NULL_CHAR*2+chr(39)+NULL_CHAR*5

keyboard[" "] = NULL_CHAR*2+chr(44)+NULL_CHAR*5
keyboard[","] = NULL_CHAR*2+chr(54)+NULL_CHAR*5
keyboard["."] = NULL_CHAR*2+chr(55)+NULL_CHAR*5
keyboard["-"] = NULL_CHAR*2+chr(45)+NULL_CHAR*5
keyboard["("] = chr(32)+NULL_CHAR+chr(38)+NULL_CHAR*5
keyboard[")"] = chr(32)+NULL_CHAR+chr(39)+NULL_CHAR*5
keyboard[";"] = NULL_CHAR*2+chr(51)+NULL_CHAR*5
keyboard[":"] = chr(32)+NULL_CHAR+chr(51)+NULL_CHAR*5
keyboard["'"] = NULL_CHAR*2+chr(52)+NULL_CHAR*5
keyboard["\""] = chr(32)+NULL_CHAR+chr(52)+NULL_CHAR*5



keyboard["\n"] = NULL_CHAR*2+chr(40)+NULL_CHAR*5
keyboard["\t"] = NULL_CHAR*2+chr(43)+NULL_CHAR*5

keyboard["__ENTER__"] = NULL_CHAR*2+chr(40)+NULL_CHAR*5
keyboard["__BACKSPACE__"] = NULL_CHAR*2+chr(42)+NULL_CHAR*5

keyboard["__UPARROW__"] = NULL_CHAR*2+chr(82)+NULL_CHAR*5
keyboard["__DOWNARROW__"] = NULL_CHAR*2+chr(81)+NULL_CHAR*5
keyboard["__LEFTARROW__"] = NULL_CHAR*2+chr(80)+NULL_CHAR*5
keyboard["__RIGHTARROW__"] = NULL_CHAR*2+chr(79)+NULL_CHAR*5

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
        fd.write((NULL_CHAR*8).encode())

def send(string):
    if string == "__ENTER__" or string == "__BACKSPACE__" or string == "__UPARROW__" or string == "__DOWNARROW__" or string == "__LEFTARROW__" or string == "__RIGHTARROW__":
        write_report(keyboard[string])
        return

    for element in string:
        write_report(keyboard[element])

#############################################

send("Hello world")
time.sleep(1)
send("__ENTER__")

