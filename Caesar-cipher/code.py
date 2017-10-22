import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "

# create `letters` here!
letters = dict(enumerate(alphabet, 0))



##
alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

#key = 3
encryption_key=3
# define `coded_message` here!
encoding= {}

        
key = (encryption_key)%27
for let in alphabet:
        encoding.update({let : key})
        key =(key + 1)%27

del encoding[' ']



##################

message = "hi my name is caesar"

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
        ty = letters[encoding[l]]
        encoded_mess = encoded_mess + (ty)
        
    
    
    return encoded_mess
    
    
encoded_message = (caesar(message,encryption_key = 3))
print(encoded_message)





decoded_message = (caesar(encoded_message,encryption_key=-3))
print(decoded_message)
        
        
