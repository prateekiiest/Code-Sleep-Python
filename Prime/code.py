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


def is_prime(num):
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True


def prime(range_from, range_to):
    allList = [num for num in range(range_from, range_to + 1) if is_prime(num)]

    print("Prime List Between", range_from, "and", range_to, "is")
    print(allList)
  
  
if __name__ == "__main__":
    print("Enter the range of number")
    range_from = int(input("From: "))
    range_to = int(input("To: "))

    prime(range_from, range_to)
    SieveOfEratosthenes(range_to)
