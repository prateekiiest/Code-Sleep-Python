from math import sqrt, ceil





def sieve_eratosthenes(range_to):
    """
    A Very efficient way to generate all prime numbers upto a number.

    Space complexity: O(n)
    Time complexity: O(n * log(logn))

    n = the number upto which prime numbers are to be generated.
    """

    # creating a boolean list first
    prime = [True for i in range(range_to + 1)]
    p = 2
    while (p * p <= range_to):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, range_to + 1, p):
                prime[i] = False

        p += 1

    # return the list of primes
    return [p for p in range(2, range_to + 1) if prime[p]]


def is_prime(num):
    """
        Returns true is the number is prime.

        To check if a number is prime, we need to check
        all its divisors upto only sqrt(number).

        Reference: https://stackoverflow.com/a/5811176/7213370
    """

    # corner case. 1 is not a prime
    if num == 1:
        return False

    # check if for a divisor upto sqrt(number)
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


def prime(range_from, range_to):
    """
    Brute Force. O(l * sqrt(num)) [l = range_to - range_from]

    Returns list of primes in the given range, by checking
    if the number is a prime or not.
    """
    return [num for num in range(range_from, range_to + 1) if is_prime(num)]


if __name__ == "__main__":
    print("Enter the range of number")
    range_from = int(input("From: "))
    range_to = int(input("To: "))

    print("Primes in the range: ", sieve_eratosthenes(range_to))
    
