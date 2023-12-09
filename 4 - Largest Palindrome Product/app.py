# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_a_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def main():
    number_of_digits = 3
    maximum_number = 10 ** number_of_digits
    largest_palindrome = 0

    for i in range(maximum_number):
        for j in range(maximum_number):
            product = i * j
            is_palindromic = is_a_palindrome(str(product))

            if is_palindromic and product > largest_palindrome:
                largest_palindrome = product

    print(largest_palindrome)


if __name__ == '__main__':
    main()
