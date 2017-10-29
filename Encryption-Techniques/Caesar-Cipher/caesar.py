#!/usr/bin/env python
import sys
from string import punctuation

def remove_punctuation(content):
	content = content.translate(None, punctuation); #removing !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
	content = ''.join(content.split()) #removing tabs, spaces, newlines
	return content.lower()

def take_input():
	try:
		k = int(raw_input("Enter key: "))
		return k
	except Exception as e:
		print "Error : ", e
		sys.exit(0)

def file_input():
	try:
		fp = open(raw_input("Enter file: "), "r")
		content = fp.read()
		fp.close()
		return content
	except Exception as e:
		print "Error : ", e
		sys.exit(1)

def display_format(message):
	'''	Print the final encoded message in blocks of five letters and ten blocks per line.
		The last line may be shorter than five blocks, and the last block may be shorter
		than five letters. '''
	output = []
	enc = ""
	while message:
		output.append(message[:5])
		message = message[5:]
	for index, block in enumerate(output):
		if((index + 1) % 10 == 0):
			enc = enc + block + "\n"
		else:
			enc = enc + block + " "
	return enc

def encrypt(content, k):
	encrypted_message = ""
	print "Discarding the punctuation..."
	content = remove_punctuation(content)
	print "Encrypting the text..."
	for char in content:
		encrypted_message += chr((ord(char) - ord('a') + k)%26 + ord('a')) #ord func gives ascii value #chr func gives character
	encrypted_message = display_format(encrypted_message)
	return encrypted_message

def decrypt(content):
	content = remove_punctuation(content)
	print "Decryting the text with each key and writing to the file \"decrypt.output\"..."
	try:
		fp = open("decrypt.output", "w");
		for k in range(26):
			plain_text = ""
			for char in content:
				plain_text += chr((ord(char) - ord('a') - (k+1))%26 + ord('a')) #ord func gives ascii value #chr func gives character
			plain_text = display_format(plain_text)
			fp.write("Key " + str(k+1) + " :\n")
			fp.write(plain_text + "\n\n")
		fp.close()
	except Exception as e:
		print "Error : ", e

def main():
	try:
		case = int(raw_input("1 to encrypt plain_text from file\n2 to decrypt ciphertext from file\nEnter option : "))
		if(case == 1):
			k = take_input()
			file_content = file_input()
			encrypted_message = encrypt(file_content, k)
			print "Encrypted Message..."
			print encrypted_message
			sys.exit(0)
		if(case == 2):
			encrypted_message = file_input()
			decrypt(encrypted_message)
			sys.exit(0)
		else:
			print "Wrong option"
			sys.exit(0)
	except KeyboardInterrupt:
		print "\nClosing the program..."
		sys.exit(0)

if __name__ == '__main__':
	main()
