"""
Author: Aditya Jain
Contact: adityajn105@gmail.com
"""
from random import shuffle
from queue import PriorityQueue
import curses
import time


class Puzzle(object):
	def __init__(self,board=None,moves=0,previous=None):
		"""
			Heuristic = manhattendistance + moves
		"""
		if board==None:
			self.board=self.generateRandomboard()
		else:
			self.board=board
		self.moves=moves
		self.previous=previous

	def generateRandomboard(self):
		x = list(range(0,9))
		x[0]=" "
		shuffle(x)
		return x

	def __str__(self):
		return """

	            |=======|=======|=======|
	            |       |       |       |
	            |   {}   |   {}   |   {}   |
	            |       |       |       |
	            |=======|=======|=======|
	            |       |       |       |
	            |   {}   |   {}   |   {}   |
	            |       |       |       |
	            |=======|=======|=======|
	            |       |       |       |
	            |   {}   |   {}   |   {}   |
	            |       |       |       |
	            |=======|=======|=======|
	    
	            	moves : {}
	    """.format(self.board[0],
	    	self.board[1],
	    	self.board[2],
	    	self.board[3],
	    	self.board[4],
	    	self.board[5],
	    	self.board[6],
	    	self.board[7],
	    	self.board[8],
	    	self.moves)

	def __eq__(self,other):
		"""
			check equality of self with other board
		"""
		if other==None:
			return False
		return self.board==other.board

	def isSolution(self):
		"""
		return True if current board is goal
		"""
		return self.board==[1,2,3,4,5,6,7,8,' ']

	def manhattendistance(self):
		"""
			return difference of cols and rows of curr and goal pos of all tiles
			this is called manhatten distance
		"""
		dist = 0
		for i in range(0,9):
			if self.board[i] == " ":
				rowd = abs(2 - int(i/3))
				cold = abs(2 - i%3)
				dist += (rowd+cold)
			else:
				rowd = abs(int((self.board[i]-1)/3) - int(i/3))
				cold = abs((self.board[i]-1)%3 - i%3)
				dist += abs(rowd+cold)
		return dist

	def move_tile(self,directn):
		"""
			call exchange tile if exchange is possible
			do nothing if not possible
		"""
		pos_blank = self.find_blank()
		if directn=="up":
			if pos_blank > 3:
				self.exchange(pos_blank-1,pos_blank-4)
		elif directn=="left":
			if pos_blank%3 != 1:
				self.exchange(pos_blank-1,pos_blank-2)
		elif directn=="right":
			if pos_blank%3 != 0:
				self.exchange(pos_blank-1,pos_blank)
		else:
			if pos_blank < 7:
				self.exchange(pos_blank-1,pos_blank+2)

	def exchange(self,i,j):
		"""
			exchange tiles
			and increase move by 1
		"""
		self.board[i],self.board[j] = self.board[j],self.board[i]
		self.moves+=1

	def find_blank(self):
		"""
			return position of blank tile
		"""
		for i in range(0,9):
			if self.board[i]==" ":
				return i+1

	def clone(self):
		"""
			return new puzzle with board same as curr board
			keep move as same
			previous is same as curr board
			this is used before moving a tile
		"""
		return Puzzle(board = self.board.copy(),moves=self.moves,previous=self)


	def getNeighbors(self):
		"""
			make all possible moves in curr board
			and return it in a array
		"""
		neighbors = []
		pos_blank = self.find_blank()
		if pos_blank > 3:
			new_board = self.clone()
			new_board.move_tile("up")
			neighbors.append(new_board)

		if pos_blank%3 != 1:
			new_board = self.clone()
			new_board.move_tile("left")
			neighbors.append(new_board)

		if pos_blank%3 != 0:
			new_board = self.clone()
			new_board.move_tile("right")
			neighbors.append(new_board)

		if pos_blank < 7:
			new_board = self.clone()
			new_board.move_tile("down")
			neighbors.append(new_board)
		return neighbors

	def getvictorySign(self):
		return """





		                |=======================|
		                |                       |
		                |                       |
		                |                       |
		                |       You Won!!       |
		                |                       |
		                |                       |
		                |                       |
		                |=======================|






		        	Press \u21b3 (ENTER Key) to start new Puzzle







		"""

	def printControls(self):
		return """
		            \u2191  -> Move Up
		            \u2193  -> Move Down
		            \u2190  -> Move Left
		            \u2192  -> Move Right
		             x  -> Declare Non Solvable
		             n  -> New Puzzle
		             a  -> Automate
		"""

	def totalInversions(self):
		"""
		odd no of inversions means problem is not solvable
		"""
		inversions = 0
		nboard = self.board.copy()
		nboard.remove(' ')
		for i in range(0,8):
			for j in range(i+1,8):
				if nboard[i]>nboard[j]:
					inversions+=1
		return inversions


	def in_priority_queue(self,count):
		"""
		count is used in case 1st entry of tuple is equal
		priorityqueue uses 2nd entry of tuple to sort, in case 1st entry is equal
		third entry in tuple can't be compared to sort entries thats why we are using count
		"""
		return (self.manhattendistance()+self.moves,count,self)


def automate(board,window):
	queue = PriorityQueue()
	
	#odd inversion is not solvable
	if board.totalInversions()%2==1:
		window.clear()
		window.insstr(0,0,
			"""
			____________________________
			|  Problem is not Solvable |
			|     (Odd Inversions)     |	
			----------------------------
			""")
		window.refresh()
		time.sleep(1)
		window.getch()
		return 
	queue.put(board.in_priority_queue(0))
	path = []
	i=1
	while not queue.empty():
		bestboard = queue.get()[2]
		if not bestboard.isSolution():
			for neighbor in bestboard.getNeighbors():
				if neighbor != bestboard.previous:
					queue.put(neighbor.in_priority_queue(i))
					i+=1
		else:
			path.append(bestboard)
			prev = bestboard.previous
			while prev is not None:
				path.append(prev)
				prev = prev.previous
			break

	path.reverse()
	for board in path:
		window.clear()
		window.insstr(0,0,str(board))
		window.refresh()
		time.sleep(1.5)

	window.insstr(18, 0, "\t\tPress \u21b3 (ENTER Key) to Continue" )
	window.refresh()
	window.getch()

def initialize(window):
	board = Puzzle()
	window.insstr(0, 0, str(board))
	window.insstr(18,0,board.printControls())
	ch = window.getch()
	while str(ch)!='10':
		if ch==curses.KEY_UP:
			board.move_tile("up");
		elif ch==curses.KEY_DOWN:
			board.move_tile("down")
		elif ch==curses.KEY_LEFT:
			board.move_tile("left")
		elif ch==curses.KEY_RIGHT:
			board.move_tile("right")
		elif ch==ord("n"):
			board =Puzzle(None)
		elif ch == ord("x"):
			window.clear()
			if board.totalInversions()%2==1:
				window.insstr(0,0,board.getvictorySign())
				board = Puzzle()
			else:
				window.insstr(0,0,
				"""
			____________________________
			|   Problem is solvable!!  |
			----------------------------

			Press \u21b3 (ENTER Key) to Continue
				""")
			window.refresh()
			window.getch()
		elif ch == ord("a"):
			window.clear()
			window.insstr(0,0,
				"""
			____________________________
			|Searching Optimal Solution|
			----------------------------
				""")
			window.refresh()
			time.sleep(1)
			automate(board,window)
			board = Puzzle()

		window.clear()
		if board.isSolution():
			window.insstr(0,0,board.getvictorySign())
			window.getch()
			board = Puzzle()
		else:
			window.insstr(0, 0, str(board))
			window.insstr(18, 0, board.printControls())
			ch = window.getch()
		window.refresh()

if __name__=='__main__':
	curses.wrapper(initialize)