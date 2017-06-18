#! /usr/bin/env python

from sys import argv

arg1, arg2, arg3 = argv


def bin_to_string(argument):
    
	switcher = {
        b'\x00': "#",
        b'\x01': " ",
        b'\x02': "K",
		b'\x03': "P",
		b'\x04': "$",
		b'\x05': "N",
		b'\x06': "!",
		b'\x07': "^",
		b'\x08': "&",
		b'\x09': "~",
    }
	
	return switcher.get(argument, "nothing")

#Read In Binary File. (Start at 0x00280)

start = 0x280
#end = 0xe82
file = arg2
theend = int(float(arg3))

f = open(file, "rb")
f.seek(start)
string_of_bytes = ""
sting_from_byte = ""

try:
	byte = f.read(1)
	for outer in range(0,theend):
		for num in range(0,7):#end-start):
			#print(str(num) + ": " + str(byte) + " ")
						
			sting_from_byte = bin_to_string(byte)
			
			if(sting_from_byte=="P"):
				f.read(1)
			elif(sting_from_byte=="N"):
				f.read(1)
			elif(sting_from_byte==" "):
				f.read(1)
			elif(sting_from_byte=="^"):
				f.read(1)

			string_of_bytes += sting_from_byte
			byte = f.read(1)
		print(string_of_bytes + " :End")
		string_of_bytes = ""
	f.read(0)
finally:
	f.close()
