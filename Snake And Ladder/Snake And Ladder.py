import random as rnd 
import numpy as np 

#Function that returns dice number

def DiceNumber():
	dn=rnd.randint(1,6);
	if(dn==6):
		return dn + DiceNumber()	#If dice number is 6 it will recursively call dice number until dice number is not 6
	else:
		return dn 					#this returns dice number which isnt 6


# Snake and Ladder game
# make an array of snakes and ladders which will hold the ladders links and snake links
# The links are randomized every game and a new board is generated 


nl=int(input("Enter number of ladders links"))  #snakes and ladders will have unequal number of links

#Ladder array
#2 random numbers are chosen and are appended to the numly array
#The second number in the array is greater than the first number

ladders =np.zeros([nl,2])				#initialinz ladder links array


#temp1 and temp2 are for appending a 2 element array int to existing array of ladders or snakes

for i in range (0,nl):
	temp1=rnd.randint(0+5*i,80)      #any number between 5*number loops executed and 80
	temp2=rnd.randint(temp1,99)		 #any number between temp1 generated last step and end of board 
	ladders[i][0]=temp1
	ladders[i][1]=temp2

print(ladders)
print("\n")
ladders

#Snake array
#2 random numbers are chosen and are appended to the numpy array
#The second number in the array is lesser than the first number
#the process is the same. But now temp2 is assigned the first value

ns=int(input("Enter number of snake links"))  #number 

snakes =np.zeros([ns,2])				#initialinz snake links array

#temp1 and temp2 are for appending a 2 element array int to existing array of snakes

for i in range (0,ns):
	temp1=rnd.randint(0+5*i,80)      #any number between 5*number loops executed and 80
	temp2=rnd.randint(temp1,99)		 #any number between temp1 generated last step and end of board 
	snakes[i][0]=temp1
	snakes[i][1]=temp2

print(snakes)
print("\n")


#Board and board descisions

board=np.arange(1,101)  			#creating board of 100 positions

num_players=int(input("\nEnter number of players : "))		#To accept number of players playing

pos=np.ones(num_players)

highest=1				#initial position of all players as one

while highest<101:			#player who reaches position 100 first wins
	for i in range (0,num_players):				#iteration for all players
		move=DiceNumber()					#getting movement value from DiceNumber
		pos[i]+=move 						
		for j in range (0,nl):				#if the new position is on a ladder start then position is changed to ladder end
			if(pos[i]==ladders[j][0]):
				pos[i]=ladders[j][1]
				print("Player ",i+1," Climbs!")				
		for j in range (0,ns):				#if the new position is on a snake face then position is changed to snake tail
			if(pos[i]==snakes[j][0]):
				pos[i]=snakes[j][1]
				print("Player ",i+1," Falls!")


		if(pos[i]>highest):					#person with the highest position is given the winner tag
			highest=pos[i]
			winner=i

	print(pos)							#to see positions in each turn
	print("\n")

print("\nWinner is ",i)



