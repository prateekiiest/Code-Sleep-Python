import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.

# create `letters` here!



##
alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

# define `coded_message` here!



##################

message = raw_input("Enter a string: ")

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
    
    
encryption_key=input("Enter a number: ")
    
encoded_message = (caesar(message,encryption_key))
print(encoded_message)


decoded_message = (caesar(encoded_message,-1*encryption_key))
print(decoded_message)
