# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see the 6th prime is 13.
# What is the 10001st prime number?
import math


def is_prime(number: int) -> bool:
    ceiling_root = math.ceil(math.sqrt(number))

    for i in range(2, ceiling_root + 1):
        if number % i == 0:
            return False

    return True


def main():
    primes = []
    prime_count = 0
    number = 2

    while prime_count < 10000:
        is_prime_number = is_prime(number)

        if is_prime_number:
            primes.append(number)
            prime_count += 1

        number += 1

    print(primes.pop())


if __name__ == '__main__':
    main()
