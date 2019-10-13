#!/bin/python3
# Primitive implementaion of BlockChain Concept

import hashlib as hasher
import datetime as date

# Block structure


class Block():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashBlock()

# Create hash of block
    def hashBlock(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode())
        return sha.hexdigest()


# Create genesis block

def createGenesisBlock():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

# Create chain of blocks


def nextBlock(lastBlock):
    id = lastBlock.index + 1
    timeStp = date.datetime.now()
    data = "Block number: " + str(id)
    hash256 = lastBlock.hash
    return Block(id, timeStp, data, hash256)


# Create blockchain and add genesis block

blockchain = [createGenesisBlock()]
previousBlock = blockchain[0]


# How many blocks to add after genesis block
noOfBlocks = 20

# Add blocks to chain
for i in range(0, noOfBlocks):
    #    print(f"i value: {i}")
    addBlock = nextBlock(previousBlock)
    blockchain.append(addBlock)
    previousBlock = addBlock
    # Broadcast
    print(f"Block #{addBlock.index} has been added to blockchain!")
    print(f"Hash: {addBlock.hash} \n")
