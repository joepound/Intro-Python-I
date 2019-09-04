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
        A 'sieve' of numbers from 1 to n represented by an array of Booleans.
        1 is a placeholder for the array to make the indices even out.
        """
        sieve = [True for i in range(num + 1)]

        """
        This 'cursor' will be multiples of a prime.
        This value will be used to comb the sieve for non-primes.
        If cursor hits the index with index == num, then number is not prime.
        """
        cursor = 2

        # Set to True initially; will be False if the cursor hits index == num
        isPrime = True

        """
        If cursor becomes greater than the number's square root, then it will
        never be a multiple of it, so end the loop to skip useless iterations
        """
        while cursor ** 2 <= num and isPrime:
            # If value is True, then the number is prime
            if sieve[cursor]:
                """
                Since the number is prime, that means that its subsequent
                multiples are composite. Marks the corresponding indices as
                False to indicate this.
                """
                for i in range(cursor * 2, num + 1, cursor):
                    if i == num:
                        isPrime = False
                        break

                    # Mark number as non-prime to skip excess loop iterations
                    sieve[i] = False
            cursor += 1
        print(f"{num} is prime." if isPrime else f"{num} is composite.")
except Exception as error:
    print(ERROR_MSG if error.__str__() == "" else error)
