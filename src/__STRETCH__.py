"""
=======================
|| STRETCH CHALLENGE ||
=======================

Check if a number is prime.
    - the algorithm to be implemented is the Sieve of Erastothenes
    - a command line argument will be taken in
    - exception handling will be implemented if the argument passed
      in is not a natural number
"""

import sys
import math

ERROR_MSG = "Invalid arguments (expected a single natural number)"

try:
    # First system argument is the file being accessed (ex.: "__STRETCH__.py"),
    # so disregard it.
    if len(sys.argv) != 2:
        raise Exception("")
    num = int(sys.argv[1])
    if num < 0:
        raise Exception("")
    if num == 0 or num == 1:
        print(f"Number {num} is neither prime nor composite")
    else:
        """
        To be used for ranges -> num + 1 to ensure that num is included.
        Avoid repetitive invocations of len function or num + 1 operation.
        """
        sieve_size = num + 1

        """
        A 'sieve' of numbers from 1 to n represented by an array of Booleans.
        1 is a placeholder for the array to make the indices even out.
        """
        sieve = [True for i in range(sieve_size)]

        """
        This 'cursor' will be multiples of a prime.
        This value will be used to comb the sieve for non-primes.
        If cursor hits the index with index == num, then number is not prime.
        """
        cursor = 2

        """
        If cursor becomes greater than the number's square root, then it will
        never be a multiple of it, so end the loop to skip useless iterations.
        """
        cursor_limit = math.sqrt(num)

        """
        This is a flag to check if num has been found to not be a prime.
        This is intended for saving time on pointless iterations.
        It is set to True initially; will be False if cursor hits index == num.
        """
        isPrime = True
        while cursor <= cursor_limit and isPrime:
            # If value is True, then the number is prime
            if sieve[cursor]:
                """
                Since the number is prime, that means that its subsequent
                multiples are composite. Marks the corresponding indices as
                False to indicate this.
                """
                for i in range(cursor * 2, sieve_size, cursor):
                    if i == num:
                        isPrime = False
                        break

                    # Mark number as non-prime to skip excess loop iterations
                    sieve[i] = False
            cursor += 1
        print(f"{num} is prime." if isPrime else f"{num} is composite.")
except Exception as error:
    print(ERROR_MSG if error.__str__() == "" else error)
