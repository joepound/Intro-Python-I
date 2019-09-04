"""
=======================
|| STRETCH CHALLENGE ||
=======================

Check if a number is prime.
    - the algorithm to be implemented is the Sieve of Erastothenes.
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
        # A 'sieve' of numbers from 2 to n
        sieve = [True for i in range(num + 1)]

        # This 'cursor' is a multiple that will combe the sieve for non-primes
        cursor = 2

        # Set to true initially; will be false if the cursor hits it
        isPrime = True

        # If cursor becomes greater than the number's square root, then it will
        # never be a multiple of it, so end the loop to skip useless iterations
        while cursor ** 2 <= num and isPrime:
            print(cursor)
            # If value is true, then the number is prime
            if sieve[cursor]:
                # Since the number is prime, subsequent multiples are composite
                for i in range(cursor * 2, num + 1, cursor):
                    if i == num:
                        isPrime = False
                        break

                    # Mark number as non-prime to skip excess loop iterations
                    sieve[i] = False
            cursor += 1

        print(f"{num} is prime." if isPrime else f"{num} is composite.")
except Exception as error:
    print(ERROR_MSG if str(error) == "" else error)
