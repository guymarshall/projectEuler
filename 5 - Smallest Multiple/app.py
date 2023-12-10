# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?


def is_divisible_by(number: int, limit: int) -> bool:
    for i in range(2, limit + 1):
        if number % i != 0:
            return False

    return True


def main():
    limit: int = 20
    number_found: bool = False
    counter: int = 1

    while not number_found:
        if is_divisible_by(counter, limit):
            number_found = True
            print(counter)
        else:
            counter += 1


if __name__ == '__main__':
    main()
