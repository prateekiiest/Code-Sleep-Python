#!/usr/bin/env python
import sys
alphabets = list('abcdefghijklmnopqrstuvwxyz.,!')
def col_wise(matrix,i):								# access the matrix column wise
	return [row[i] for row in matrix]

def creat_key_num(key):								# function to create key numbering
	l1 = list(key)
	l1.sort()
	l = {}
	for i in range(len(key)):
		l[key[i]] = l1.index(key[i])
	return l

def generate_matrix(content, rows, cols):			#function to generate matrix of given text
	matrix = [[0]]*rows	 							#initializing a matrix with zeros
	k = 0
	for i in range(rows):
		row = []
		for j in range(cols):
			if(k != len(content)):
				row.append(content[k])          #alphabets.index(content[k])
				k+=1
			else:
				row.append(" ")
		matrix[i] = row
	return matrix

def encrypt(message, key):						 #encryption function
	cipher = ''
	cols = len(key)
	rows = len(message) / cols
	if(len(message) % cols != 0):
		rows = rows+1
	matrix = generate_matrix(message,rows,cols)
	key_num = creat_key_num(key)
	for i in range(len(key)):
		j = key_num[key[i]]
		cipher += ''.join(col_wise(matrix,j))
	return cipher

def decrypt(ciphertext, key):							#decryption function
	temp = {}
	cipher = []
	dicipher = ''
	cols = len(key)
	rows = len(ciphertext) / cols
	if(len(ciphertext) % cols != 0):
		rows = rows+1
	matrix = generate_matrix(ciphertext,cols,rows)
	for i in range(len(key)):
		temp[key[i]] = matrix[i]
	for i in sorted(temp):
		cipher.append(temp[i])
	for i in range(rows):
		dicipher += ''.join(col_wise(cipher,i))
	return dicipher

def main():
	try:
		case = int(raw_input("1 to encrypt plain_text\n2 to decrypt ciphertext\nEnter option : "))
		if(case == 1):
			k = raw_input("Enter key: ")
			if(len(k) == 0):
				print("Enter key atleast of size 1...")
				sys.exit(0)

			message = raw_input("Message[Plain Text]: ")

			print "Key numbering: ",
			key_num = creat_key_num(k)

			for i in list(k):
				print key_num[i],
			print ' '
			encrypted_message = encrypt(message, k)
			print "Encrypted Message :"
			print encrypted_message
			sys.exit(0)
		if(case == 2):
			k = raw_input("Enter key: ")
			if(len(k) == 0):
				print("Enter key atleast of size 1...")
				sys.exit(0)
			encrypted_message = raw_input("Ciphertext: ")
			plain_text = decrypt(encrypted_message, k)
			print "Decrypted Message :"
			print plain_text
			sys.exit(0)
		else:
			print "Wrong option"
			sys.exit(0)
	except KeyboardInterrupt:
		print "\nClosing the program..."
		sys.exit(0)

if __name__ == '__main__':
	main()
