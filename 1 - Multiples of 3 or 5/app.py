# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    limit = 1000
    multiples_of_3 = {number * 3 for number in range(limit + 1) if number * 3 < limit}
    multiples_of_5 = {number * 5 for number in range(limit + 1) if number * 5 < limit}
    sum_of_multiples = sum(multiples_of_3 | multiples_of_5)
    print(sum_of_multiples)


if __name__ == '__main__':
    main()
