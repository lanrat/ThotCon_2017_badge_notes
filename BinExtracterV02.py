#! /usr/bin/env python3

from sys import argv
import sys

arg1, arg2, arg3 = argv


def bin_to_string(argument):
    
	switcher = {
        b'\x00': "#",
        b'\x01': " ",
        b'\x02': "K",
		b'\x03': "P",
		b'\x04': "$",
		b'\x05': "D",
		b'\x06': "!",
		b'\x07': "^",
		b'\x08': "&",
		b'\x09': "~",
    }
	
	return switcher.get(argument, "None")

#Read In Binary File. (Start at 0x00280)

start = 0x281
start = 0x4f6
file = arg2
theend = int(float(arg3))

f = open(file, "rb")
f.seek(start)
string_of_bytes = ""
sting_from_byte = ""

i = 0

try:
	byte = f.read(1)
	for layer in range(1,theend+1):
		print(" "*16+"   A     B     C     D     E     F     X     Z")
		print(" "*16+"#"*49)

		for y in range(8):
			for num in range(8):#end-start):
				#print(str(num) + ": " + str(byte) + " ")
							
				sting_from_byte = bin_to_string(byte)
				i +=1
				if string_of_bytes == "None":
					print("Done!")
					sys.exit()
				
				string_of_bytes += sting_from_byte
				byte = f.read(1)
			print(" "*16+"#     "*8+"#")
			print(" "*16+"#  {}  #  {}  #  {}  #  {}  #  {}  #  {}  #  {}  #  {}  # {}".format(string_of_bytes[0],string_of_bytes[1],string_of_bytes[2],string_of_bytes[3],string_of_bytes[4],string_of_bytes[5],string_of_bytes[6],string_of_bytes[7], y+1))
			print(" "*16+"#     "*8+"#")
			print(" "*16+"#"*49)
			string_of_bytes = ""
		if layer == 1:
			layer = 0
		print("\n|[L3V3L: {}] | [Layer: {}] | [Origin: F 4] | [KEY] | [Serial:Connected] |  VT100 |".format(layer/8, layer%8))
		print("\n")
	f.read(0)
finally:
	f.close()
