#!/usr/bin/env python
import argparse
import aes
import sys

def bytes2int(data):
	return int(data.encode('hex'), 16)

def hex2bytes(data):
	hex_val = hex(data)[2:-1].zfill(32)
	return bytearray.fromhex(hex_val)

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="File to encrypt or decrypt", type=argparse.FileType('rb'))
parser.add_argument("key_file", help="File containing key", type=argparse.FileType('rb'))
parser.add_argument("output_file", help="File to write output", type=argparse.FileType('wb', 0))
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e", "--encrypt", action="store_true", help="Encrypt input file")
group.add_argument("-d", "--decrypt", action="store_true", help="Decrypt input file")
args = parser.parse_args()

key = bytes2int(args.key_file.read(16))
Aes = aes.AES(key)

if(args.encrypt):
	print "AES encrypting ..."
	action = lambda x: Aes.encrypt(x)
elif(args.decrypt):
	print "AES decrypting ..."
	action = lambda x: Aes.decrypt(x)
else:
	print "Wrong input arguments"
	sys.exit()

while(True):
	input_bytes = args.input_file.read(16)
	if(input_bytes == ''):
		break
	input_int = bytes2int(input_bytes)
	output_int = action(input_int)
	output_bytes = hex2bytes(output_int)
	args.output_file.write(output_bytes)

print "Operation was successful."
