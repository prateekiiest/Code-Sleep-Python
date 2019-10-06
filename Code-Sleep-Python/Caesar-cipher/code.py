import string
string.ascii_lowercase
import argparse

# We will consider the alphabet to be these letters, along with a space.

# create `letters` here!



##
alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

p = argparse.ArgumentParser(description="Make line of colored text look like an Image")
p.add_argument("-e", "-encription_key", help="encription key")
p.add_argument("-m", "-message", help="message")
args = p.parse_args()


##################

message = args.m

def caesar(mee, encryption_key):
        
    encoding= {}

        
    key = (encryption_key)%27
    for let in alphabet:
        encoding.update({let : key})
        key =(key + 1)%27
    #del encoding[" "]

    encoded_mess = ""
   # me = message.replace(" ","")
    # return the encoded message as a single string!
    for l in mee:
    	if(l!=' '):
    		ty = letters[encoding[l]]
    	    	encoded_mess = encoded_mess + (ty)
    		    	    
    	else:
    		encoded_mess = encoded_mess + ' '
    			
        
    return encoded_mess
    
    
encryption_key = args.e
    
encoded_message = (caesar(message,encryption_key))
print(encoded_message)


decoded_message = (caesar(encoded_message,-1*encryption_key))
print(decoded_message)
