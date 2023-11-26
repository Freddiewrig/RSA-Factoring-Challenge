#!/usr/bin/env python3

import sys
def factorize(n):
    """
    Factorize a file into a list of prime factors.

    Parameters:
    n(int): the number to factorize

    Return:
    a list of factors
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
        if n > 1:
            factors.append(n)
        return (factors)
def main(filename):
    """
    Factorize numbers from a file and print their factorizations.

    Parameters:
    filename (str): The name of the file containing natural numbers to factor.

    output:
    Prints the factorization of each number in the format "n=p*q" where p and
    q are factors.
    """
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors_list = factorize(number)
            factors_str = '*'.join(map(str, factors_list))
            print(f"{number}={factors_str}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
