from readfiles import *
from AES256 import *
import argparse
from argparse import RawTextHelpFormatter
import time

parser = argparse.ArgumentParser(description='AES 256-bit encrypt and decrypt', formatter_class=RawTextHelpFormatter)
parser.add_argument('mode',help="encrypt or decrypt")
args = parser.parse_args()

mode = str(args.mode).lower()

def fileEncrypt():
	block = getEncryptBlock("testBlock")
	key = getKey("testKey")
	outfile = open("encrypted_file","wb")
	strangen = ""
	cryptLargeblock = []
	for i in range(len(block)):
		cryptLargeblock.append(encrypt(block[i],key))

	while i < len(cryptLargeblock):
		for row in cryptLargeblock:
			for item in row:
				strangen += hex(item)[2:].zfill(2)
		i += 1
	outfile.write(strangen)
	outfile.close()
	print strangen

def fileDecrypt():
	key = getKey("testKey")
	file = open("decrypted_file","wb")
	decryptBlock = []
	decString = ""
	eblock = getDecryptBlock("encrypted_file")

	for i in range(len(eblock)):
		decryptBlock.append(decrypt(eblock[i],key))

	for row in decryptBlock:
		for item in row:
			decString += chr(item)

	file.write(decString)
	file.close()
	print decString

if mode == "encrypt" or mode == "e":
	fileEncrypt()
elif mode == "decrypt" or mode == "d":
	fileDecrypt()
