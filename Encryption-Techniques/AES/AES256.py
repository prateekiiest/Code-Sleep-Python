from copy import copy
from tables import *

def subBytes(block):
	for i in range(len(block)):
		block[i] = sbox[block[i]]
	return block

def subBytesInv(block):
	for i in range(len(block)):
		block[i] = sboxInv[block[i]]
	return block

def keyScheduleCore(word, i):
	newWord = word[1:]+word[:1]
	subBytes(newWord)
	newWord[0] = newWord[0] ^ rCon[i]
	return newWord

def expandKey(cipherKey):
	cipherKeySize = len(cipherKey)
	assert cipherKeySize == 32
	expandedKey = []
	currentSize,rconIter = 0,1

	t = [0,0,0,0]

	for i in range(cipherKeySize):
		expandedKey.append(cipherKey[i])
	currentSize += cipherKeySize

	while currentSize < 240:
		for i in range(4):
			t[i] = expandedKey[(currentSize - 4) + i]
		if currentSize % cipherKeySize == 0:
			t = keyScheduleCore(t, rconIter)
			rconIter += 1
		if currentSize % cipherKeySize == 16:
			for i in range(4):
				t[i] = sbox[t[i]]
		for i in range(4):
			expandedKey.append(((expandedKey[currentSize - cipherKeySize]) ^ (t[i])))
			currentSize += 1
	return expandedKey

def createRoundKey(expandedKey,i):
	return expandedKey[i*16:i*16+16]

def addroundkey(block,roundKey):
	for i in range(len(block)):
		block[i] = block[i] ^ roundKey[i]
	return block

def blockfileColumn(filename):
	test2 = filename
	testarr = []
	for row in range(0,4):
		for column in range(0,len(test2),4):
			testarr.append(test2[row+column])
	return testarr

def rotate(rotate, n):
	return rotate[n:]+rotate[0:n]

def shiftRow(blockfile):
	block = blockfileColumn(blockfile)
	for i in range(4):
		block[i*4:i*4+4] = rotate(block[i*4:i*4+4], i)
	blockDone = blockfileColumn(block)
	return blockDone

def shiftRowInv(blockfile):
	block = blockfileColumn(blockfile)
	for i in range(4):
		block[i*4:i*4+4] = rotate(block[i*4:i*4+4], -i)
	block = blockfileColumn(block)
	return block

def mixColumn(column):
	col = copy(column)
	column[0] = table_2[col[0]] ^ table_3[col[1]] ^ col[2] ^ col[3]
	column[1] = col[0] ^ table_2[col[1]] ^ table_3[col[2]] ^ col[3]
	column[2] = col[0] ^ col[1] ^ table_2[col[2]] ^ table_3[col[3]]
	column[3] = table_3[col[0]] ^ col[1] ^ col[2] ^ table_2[col[3]]
	return column


def mixColumns(col):
	outCol = []
	for i in range(0,len(col),4):
		outCol.append(mixColumn(col[i:i+4]))
	return listoflist2singlelist(outCol)

def mixColumnInv(column):
	col = copy(column)
	column[0] = table_14[col[0]] ^ table_11[col[1]] ^ table_13[col[2]] ^ table_9[col[3]]
	column[1] = table_9[col[0]] ^ table_14[col[1]] ^ table_11[col[2]] ^ table_13[col[3]]
	column[2] = table_13[col[0]] ^ table_9[col[1]] ^ table_14[col[2]] ^ table_11[col[3]]
	column[3] = table_11[col[0]] ^ table_13[col[1]] ^ table_9[col[2]] ^ table_14[col[3]]
	return column


def mixColumnsInv(col):
	intList = []
	for i in range(0,len(col),4):
		intList.append(mixColumnInv(col[i:i+4]))
	return listoflist2singlelist(intList)

def listoflist2singlelist(column):
	columnList = []
	for row in column:
		for i in range(0,len(row)):
			columnList.append(row[i])
	return columnList

def encrypt(block,key):
	expandedKey = expandKey(key)
	roundKey = createRoundKey(expandedKey,0)
	block = addroundkey(block,roundKey)

	for i in range(1,14):
		roundKey = createRoundKey(expandedKey,i)
		block = subBytes(block)
		block = shiftRow(block)
		block = mixColumns(block)
		block = addroundkey(block,roundKey)

	roundKey = createRoundKey(expandedKey,14)
	block = subBytes(block)
	block = shiftRow(block)
	block = addroundkey(block,roundKey)
	return block

def decrypt(block,key):
	expandedKey = expandKey(key)
	roundKey = createRoundKey(expandedKey,14)
	block = addroundkey(block,roundKey)
	block = shiftRowInv(block)
	block = subBytesInv(block)

	for i in range(13,0,-1):
		roundKey = createRoundKey(expandedKey,i)
		block = addroundkey(block,roundKey)
		block = mixColumnsInv(block)
		block = shiftRowInv(block)
		block = subBytesInv(block)

	roundKey = createRoundKey(expandedKey,0)
	block = addroundkey(block,roundKey)
	return block
