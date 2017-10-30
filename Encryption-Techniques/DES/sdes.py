#!/usr/bin/env python
#
# Copyright (c) 2017 by Aditya Malu adityamalu1@gmail.com. All Rights Reserved.
#
import sys
p10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
p8 = (6, 3, 7, 4, 8, 5, 10, 9)
p4 = (2, 4, 3, 1)
ip = (2, 6, 3, 1, 4, 8, 5, 7)
inverseip = (4, 1, 3, 5, 7, 2, 8, 6)
ep = (4, 1, 2, 3, 2, 3, 4, 1)
s0 = (['01', '00', '11', '10'], #[1, 0, 3, 2]
		['11', '10', '01', '00'], #[3, 2, 1, 0]
		['00', '10', '01', '11'], #[0, 2, 1, 3],
		['11', '01', '11', '10']) #[3, 1, 3, 2]
s1 = (['00', '01', '10', '11'], #[0, 1, 2, 3]
		['10', '00', '01', '11'], #[2, 0, 1, 3]
		['11', '00', '01', '00'], #[3, 0, 1, 0],
		['10', '01', '00', '11']) #[2, 1, 0, 3]

def shiftleftn(K, n):
	return K[n:] + K[:n]

def doP10(K):
	K1 = []
	for i in p10:
		K1.append(K[i-1])
	return K1

def doP8(K):
	K1 = []
	for i in p8:
		K1.append(K[i-1])
	return K1

def doEP(R):
	R1 = []
	for i in ep:
		R1.append(R[i-1])
	return R1

def doP4(R):
	R1 = []
	for i in p4:
		R1.append(R[i-1])
	return R1


def doSBOX(A):
	bintodec = {00:0, 01:1, 10:2, 11:3}
	L, R = A[:4], A[4:]
	l_row = bintodec[int(str(L[0])+str(L[3]))]
	l_col = bintodec[int(str(L[1])+str(L[2]))]
	r_row = bintodec[int(str(R[0])+str(R[3]))]
	r_col = bintodec[int(str(R[1])+str(R[2]))]
	return map(int, list(s0[l_row][l_col] + s1[r_row][r_col]))

def generate_keys(K):
	K1 = doP10(K)
	K1L = shiftleftn(K1[:5], 1)
	K1R = shiftleftn(K1[5:], 1)
	K1 = K1L + K1R
	K1 = doP8(K1)
	K2 = doP10(K)
	K2L = shiftleftn(K2[:5], 3)
	K2R = shiftleftn(K2[5:], 3)
	K2 = K2L + K2R
	K2 = doP8(K2)
	return K1, K2

def doXOR(l1, l2):
	l3 = []
	for i in range(len(l1)):
		l3.append(l1[i]^l2[i])
	return l3

def doIP(P):
	P1 = []
	for i in ip:
		P1.append(P[i-1])
	return P1

def doinverseIP(P):
	P1 = []
	for i in inverseip:
		P1.append(P[i-1])
	return P1

def F(R, K):
	R1 = doEP(R)
	xor_result = doXOR(R1, K)
	sbox_result = doSBOX(xor_result)
	X = doP4(sbox_result)
	return X

def do_fK(P, K):
	L, R = P[:4], P[4:] #fK(L, R) = (L xor F(R, SK), R)
	I = F(R, K)
	J = doXOR(L, I)
	return J + R

def encrypt(P, K):
	K1, K2 = generate_keys(K)
	P1 = doIP(P)
	P2 = do_fK(P1, K1)
	P3 = P2[4:]+P2[:4]
	P4 = do_fK(P3, K2)
	E = doinverseIP(P4)
	return E

def decrypt(C, K):
	K1, K2 = generate_keys(K)
	C1 = doIP(C)
	C2 = do_fK(C1, K2)
	C3 = C2[4:]+C2[:4]
	C4 = do_fK(C3, K1)
	D = doinverseIP(C4)
	return D

def main():
	print '-'*40
	case = int(raw_input("Option 1 to encrypt\nOption 2 to decrypt \nEnter option : "))
	## Encrypt case
	if case == 1:
		P = map(int, list(raw_input("Enter 8 bit plaintext (eg. 10100101) - "))) #8 bit plaintext
		if len(P) != 8:
			print "Enter only 8 bit plaintext!"
			sys.exit(0)

		K = map(int, list(raw_input("Enter 10 bit key (eg. 1110000110) - "))) #10 bit key
		if len(K) != 10:
			print "Enter only 10 bit key!"
			sys.exit(0)

		E = encrypt(P, K)
		print "Encrypted - ", ''.join(map(str, E))
	##
	##Decrypt case
	if case == 2:
		C = map(int, list(raw_input("Enter 8 bit ciphertext (eg. 10100101) - "))) #8 bit ciphertext
		if len(C) != 8:
			print "Enter only 8 bit ciphertext!"
			sys.exit(0)

		K = map(int, list(raw_input("Enter 10 bit key (eg. 1110000110) - "))) #10 bit key
		if len(K) != 10:
			print "Enter only 10 bit key!"
			sys.exit(0)

		D = decrypt(C, K)
		print "Decrypted - ", ''.join(map(str, D))
	##
	print '-'*40

if __name__ == '__main__':
	main()
