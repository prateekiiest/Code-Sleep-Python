import pygame,tkinter,math #importing modules
pygame.init()
num = 0
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
MAUVE = (224, 176, 255) #colour tuples to be used later in the program
clock = pygame.time.Clock()

############Getting User Input using GUI#####################
def get_num():
    global num
    num = int(n.get()) #gets value of num from Tkinter GUI
    m.destroy() #destroys root window

m = tkinter.Tk() #root window
l1 = tkinter.Label(m,text='Enter a number', width = 25) #label widget
n = tkinter.Entry(m) #entry widget

btn = tkinter.Button(m,text = 'Calculate',command = get_num) #calculate button bounded to get_num function
l1.pack()
n.pack()
btn.pack() #using pack() geometry manager
m.mainloop() #start GUI

###################Setting up grid#######################
sq_num = num
if (math.floor(math.sqrt(num))**2 - num != 0):
    sq_num = (math.floor(math.sqrt(num)) + 1)**2 #getting nearest square greater than or equal to num
dim = int(sq_num**0.5) #number of rows and columns of the window

width = 32 * dim  #creating a window having 'dim' rows and columns. Each cell has width of 32px
display = pygame.display.set_mode((width,width))
display.fill(WHITE) #fill the display with WHITE color

for i in range(0,width,32):
    pygame.draw.line(display,BLACK,(i,0),(i,width)) #drawing row lines 32px apart
for j in range(0,width,32):
    pygame.draw.line(display,BLACK,(0,j),(width,j)) #drawing column lines 32px apart
pygame.display.update()

def text_objects(text, font):
    '''
    Function to create TextSurface and TextRect objects for displaying text on the PyGame window.
    It takes 2 parameters:
        text : the text to be displayed
        font : pygame.font.Font object in which the text is to be rendered
    '''
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text,x,y,size):
    '''
    Function to display the given 'text' message at a position of (x,y) in size 'size'
    '''
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    display.blit(TextSurf, TextRect)
    pygame.display.update()

celldict = {} #dictionary to map numbers to their respective cells

class Cell: #creating a class for Cell objects on the grid
    def __init__(self,x,y,n):
        self.pos = (x,y)
        self.value = n
        self.highlighted = False
        celldict[self.value] = self #adding the number and cell pair to the celldict dictionary
        message_display(f"{self.value}",x + 16,y + 16,17) #display the value of the cell on the grid at the center of the cell

    def highlight(self):
        if not self.highlighted:
            x,y = self.pos
            pygame.draw.rect(display,MAUVE,(x,y,32,32)) #create a MAUVE rectangle on top of the cell to highlight composite numbers
            message_display(f"{self.value}",x + 16,y + 16,17) #rewrite the value of the cell on top of the MAUVE highlight
            self.highlighted = True #to avoid time to re-highlight cells that have already been highlighted
            pygame.time.wait(50) #for the effect of moving highlight or "scanning" the grid

count = 1
for i in range(0,width,32):
    pygame.event.pump() #to deal with internal PyGame events in the event queue which cause the system to freeze
    for j in range(0,width,32):
        if (count <= num):
            cell = Cell(j,i,count) #create a Cell object at every grid intersection
            clock.tick()
            count += 1
        else:
            break
pygame.display.update()
#################Sieving algorithm###################
nums = set(range(2,num+1)) #all the numbers except 1 since 1 is neither prime nor composite
composites = {1} #set of composites detected so far
celldict[1].highlight() #highlight the Cell 1

for i in range(2,round(math.sqrt(num)) + 1): #check all numbers till sqrt(num)
    if i not in composites:
        comp = [i*k for k in range(2,num//i + 1)] #cross out all the multiples of prime numbers
        composites.update(comp)
        for val in comp:
            pygame.event.pump()
            celldict[val].highlight() #highlight the composites

primetxt = '' #string of primes to be displayed
for val,cell in celldict.items():
    pygame.event.pump()
    if not cell.highlighted: #if the cell has not been highlighted, it is prime
        x,y = cell.pos
        pygame.draw.rect(display,GREEN,(x,y,32,32)) #highlight the primes with GREEN
        message_display(f"{val}",x + 16,y + 16,17)
        pygame.time.wait(100) #to create a moving highlight
        primetxt += str(val) + ' ,' #concatenate primes to primetxt string

##############Displaying results using GUI############
m = tkinter.Tk() #root window
l1 = tkinter.Label(m,text='Primes that were sieved: ')
msg = tkinter.Message(m, text = primetxt[:-1],width = 200) #Message widget to display the sieved primes
l1.pack()
msg.pack()
m.mainloop()