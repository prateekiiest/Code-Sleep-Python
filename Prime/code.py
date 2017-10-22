

def prime(range_from, range_to):
  
  allList = [x for x in range(2, int(range_to)+1)]

  ptr = 0
  while True:
    i = 2
    while i * allList[ptr] <= int(range_to):
      if i*allList[ptr] in allList:
        allList.remove(i*allList[ptr])
      i += 1
    ptr += 1
    if allList[ptr] ** 2 > int(range_to):
      break


  primeList = [x for x in allList if x > int(range_from)]
  print("Prime List Between ", range_from, " and ", range_to, " is")
  print(primeList)

  
  
if __name__ == "__main__":
  print("Enter the range of number")
  range_from = input("From: ")
  range_to = input("To: ")

  prime(range_from, range_to)
