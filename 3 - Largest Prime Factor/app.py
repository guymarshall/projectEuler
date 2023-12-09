# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
import math


def generate_factors(input_number: int) -> list:
    ceiling_root: int = math.ceil(math.sqrt(input_number))
    return [number for number in range(2, ceiling_root) if input_number % number == 0]


def is_prime(input_number: int) -> bool:
    ceiling_root: int = math.ceil(math.sqrt(input_number))
    for i in range(2, ceiling_root):
        if input_number % i == 0:
            return False

    return True


def main():
    number: int = 600_851_475_143
    factors: list = generate_factors(number)
    prime_factors = [number for number in factors if is_prime(number)]
    print(max(prime_factors))


if __name__ == '__main__':
    main()
