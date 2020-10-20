
def printpy(n):
    for i in range(0, n):

        for j in range(0, i+1):

            print("*", end=" ")

        print()


def printrevpy(n):
    for i in range(n, 0, -1):

        for j in range(0, i):

            print("*", end=" ")

        print()


print("How Many Row You Want To Print")

n = int(input())

print("Type 1 Or 0")

m = int(input())

l = bool(m)

if l == True:
    printpy(n)
elif l == False:
    printrevpy(n)
