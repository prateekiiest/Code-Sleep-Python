def SieveOfEratosthenes(range_to):

  # creating a boolean array first
  prime = [True for i in range(range_to + 1)]
  p = 2
  while (p * p <= range_to):
       
    # If prime[p] is not changed, then it is a prime
    if (prime[p] == True):
         
        # Update all multiples of p
        for i in range(p * 2, range_to + 1, p):
            prime[i] = False
    p += 1
  print([p for p in range(2, range_to) if prime[p]])

def prime(range_from, range_to):
  
  allList = [x for x in range(2, range_to + 1)]

  ptr = 0
  while True:
    i = 2
    while i * allList[ptr] <= range_to:
      if i*allList[ptr] in allList:
        allList.remove(i*allList[ptr])
      i += 1
    ptr += 1
    if allList[ptr] ** 2 > range_to:
      break


  primeList = [x for x in allList if x > range_from]
  print("Prime List Between ", range_from, " and ", range_to, " is")
  print(primeList)

  
  
if __name__ == "__main__":
  print("Enter the range of number")
  range_from = int(input("From: "))
  range_to = int(input("To: "))

  prime(range_from, range_to)
  SieveOfEratosthenes(range_to)

