#!/usr/bin/env python

#
# Copyright (c) 2017 by Aditya Malu adityamalu1@gmail.com. All Rights Reserved.
#

import sys

bin_to_int = {'0000':0, '0001':1, '0010':2, '0011':3, '0100':4, '0101':5, '0110':6 , '0111':7, '1000':8, '1001':9, '1010':10, '1011':11,
			'1100':12, '1101':13, '1110':14, '1111':15 }
int_to_bin = {0:'0000', 1:'0001', 2:'0010', 3:'0011', 4:'0100', 5:'0101', 6:'0110' , 7:'0111', 8:'1000', 9:'1001', 10:'1010', 11:'1011',
			12:'1100', 13:'1101', 14:'1110', 15:'1111' }
add_inv = {'0000':'0000', '0001':'1111', '0010':'1110', '0011':'1101', '0100':'1100', '0101':'1011', '0110':'1010' , '0111':'1001',
			'1000':'1000', '1001':'0111', '1010':'0110', '1011':'0101', '1100':'0100', '1101':'0011', '1110':'0010', '1111':'0001' }
mul_inv = {'0000':'0000', '0001':'0001', '0010':'1001', '0011':'0110', '0100':'1101', '0101':'0111', '0110':'0011' , '0111':'0101',
			'1000':'1111', '1001':'0010', '1010':'1100', '1011':'1110', '1100':'1010', '1101':'0100', '1110':'1011', '1111':'1000' }

def mul_mod_17(a1, a2):
	'''The 16 nibbles are thought of as 0001, ..., 1111, 0000, which represent 1,..., 15, 16, for multiplication modulo 17.
		Notice that 0000, which is 16, is congruent to -1 modulo 17. 0000 is its own inverse under multiplication modulo 17'''
	if a1 == 0:
		a1 = 16
	a3 = (a1 * a2) % 17
	if a3 == 16:
		a3 = 0
	return a3

def readfile(filename):
	try:
		fp = open(filename, "r")
		content = fp.read()
		return content
	except IOError:
		print "Error opening file:", filename
		sys.exit(1)

def generate_encryption_keys(key):
	key_format = []
	last_round = []
	shift_key_1 = key[6:] + key[:6]
	shift_key_2 = shift_key_1[6:] + shift_key_1[:6]
	shift_key_3 = shift_key_2[6:] + shift_key_2[:6]
	long_key = key + shift_key_1 + shift_key_2 + shift_key_3[:16]
	for i in range(4):
		round_i = []
		for j in range(6):
			round_i.append(long_key[:4])
			long_key = long_key[4:]
		key_format.append(round_i)
	for k in range(4):
		last_round.append(long_key[:4])
		long_key = long_key[4:]
	key_format.append(last_round)
	return key_format

def generate_decryption_keys(key):
	''' Bad function. Bad coding. Hard Coded.'''
	en_keys = generate_encryption_keys(key)
	de_keys, round_1, round_2, round_3, round_4, round_5 = [], [], [], [], [], []
	round_1.append(mul_inv[en_keys[4][0]])
	round_1.append(add_inv[en_keys[4][1]])
	round_1.append(add_inv[en_keys[4][2]])
	round_1.append(mul_inv[en_keys[4][3]])
	round_1.append(en_keys[3][4])
	round_1.append(en_keys[3][5])
	de_keys.append(round_1)
	round_2.append(mul_inv[en_keys[3][0]])
	round_2.append(add_inv[en_keys[3][1]])
	round_2.append(add_inv[en_keys[3][2]])
	round_2.append(mul_inv[en_keys[3][3]])
	round_2.append(en_keys[2][4])
	round_2.append(en_keys[2][5])
	de_keys.append(round_2)
	round_3.append(mul_inv[en_keys[2][0]])
	round_3.append(add_inv[en_keys[2][1]])
	round_3.append(add_inv[en_keys[2][2]])
	round_3.append(mul_inv[en_keys[2][3]])
	round_3.append(en_keys[1][4])
	round_3.append(en_keys[1][5])
	de_keys.append(round_3)
	round_4.append(mul_inv[en_keys[1][0]])
	round_4.append(add_inv[en_keys[1][1]])
	round_4.append(add_inv[en_keys[1][2]])
	round_4.append(mul_inv[en_keys[1][3]])
	round_4.append(en_keys[0][4])
	round_4.append(en_keys[0][5])
	de_keys.append(round_4)
	round_5.append(mul_inv[en_keys[0][0]])
	round_5.append(add_inv[en_keys[0][1]])
	round_5.append(add_inv[en_keys[0][2]])
	round_5.append(mul_inv[en_keys[0][3]])
	de_keys.append(round_5)
	return de_keys

def do_operations(s, round_i):
	k1, k2, k3, k4, k5, k6 = bin_to_int[round_i[0]], bin_to_int[round_i[1]], bin_to_int[round_i[2]], bin_to_int[round_i[3]], bin_to_int[round_i[4]], bin_to_int[round_i[5]]
	s1, s2, s3, s4 = bin_to_int[s[0]], bin_to_int[s[1]], bin_to_int[s[2]], bin_to_int[s[3]]
	a1 = mul_mod_17(s1, k1)
	a2 = (s2 + k2) % 16
	a3 = (s3 + k3) % 16
	a4 = mul_mod_17(s4, k4)
	a5 = a1 ^ a3
	a6 = a2 ^ a4
	a7 = mul_mod_17(a5, k5)
	a8 = (a6 + a7) % 16
	a9 = mul_mod_17(a8, k6)
	a10 = (a7 + a9) % 16
	a11 = a1 ^ a9
	a12 = a3 ^ a9
	a13 = a2 ^ a10
	a14 = a4 ^ a10
	s1, s2, s3, s4 = int_to_bin[a11], int_to_bin[a13], int_to_bin[a12], int_to_bin[a14]
	return [s1] + [s2] + [s3] + [s4]

def do_last_round(s, last_round):
	k1, k2, k3, k4 = bin_to_int[last_round[0]], bin_to_int[last_round[1]], bin_to_int[last_round[2]], bin_to_int[last_round[3]]
	s1, s2, s3, s4 = bin_to_int[s[0]], bin_to_int[s[1]], bin_to_int[s[2]], bin_to_int[s[3]]
	v1 = mul_mod_17(s1, k1)
	v2 = (s2 + k2) % 16
	v3 = (s3 + k3) % 16
	v4 = mul_mod_17(s4, k4)
	return int_to_bin[v1] + int_to_bin[v2] + int_to_bin[v3] + int_to_bin[v4]

def encrypt_decrypt(text, keys):
	s1, s2, s3, s4 = text[:4], text[4:8], text[8:12], text[12:16]
	s = [s1] + [s2] + [s3] + [s4]
	for r in range(len(keys)-1):
		s = do_operations(s, keys[r])
	last_round = keys[len(keys)-1]
	ctext = do_last_round(s, last_round)
	return ctext

def main():
	print '-'*40
	case = int(raw_input("Option 1 to encrypt\nOption 2 to decrypt \nEnter option : "))
	## Encrypt case
	if case == 1:
		key = readfile(raw_input("Enter key file: "))
		keys = generate_encryption_keys(key)
		plaintext = readfile(raw_input("Enter plaintext file: "))
		encrypted = encrypt_decrypt(plaintext, keys)
		print "Encrypted: ", encrypted
	## Decrypt case
	if case == 2:
		key = readfile(raw_input("Enter key file: "))
		de_keys = generate_decryption_keys(key)
		ciphertext = readfile(raw_input("Enter ciphertext file: "))
		detext = encrypt_decrypt(ciphertext, de_keys)
		print "Decrypted: ", detext
	print '-'*40

if __name__ == '__main__':
	main()
