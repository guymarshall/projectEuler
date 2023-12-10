# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math


def is_prime(number: int) -> bool:
    if number == 2:
        return True

    ceiling_root: int = math.ceil(math.sqrt(number))

    for i in range(2, ceiling_root + 1):
        if number % i == 0:
            return False

    return True


def main():
    start: int = 2
    finish: int = 2_000_000

    primes_below_limit: list = [number for number in range(start, finish) if is_prime(number)]

    print(sum(primes_below_limit))


if __name__ == '__main__':
    main()
