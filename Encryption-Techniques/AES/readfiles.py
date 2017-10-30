def getKey(filename):
	len_key = 64
	keyfile = open(filename, 'r')
	hexadecimalkey = keyfile.read()
	keyarray = []
	for i in range(0, len_key, 2):
		keyarray.append(int(hexadecimalkey[i:i+2], 16))
	return keyarray

def getDecryptBlock(block):
	file = open(block, 'r')
	byte = file.read()
	blockarray = []
	block = []
	for i in range(0,len(byte),2):
		blockarray.append(int(byte[i:i+2],16))

	for i in range(0,len(blockarray),16):
		block.append(blockarray[i:i+16])
	return block

def getEncryptBlock(block):
	file = open(block,'rb')
	byte = file.read().encode("hex")
	blockarray = []
	arr = []
	for i in range(0,len(byte),2):
		arr.append(int(byte[i:i+2], 16))

	while len(arr) >= 16:
		blockarray.append(arr[0:16])
		arr = arr[16:]
		if len(arr) < 16:
			temparray = [0]*16
			for k in range(0,len(arr)):
				temparray[k] = arr[k]
			blockarray.append(temparray)
	return blockarray
