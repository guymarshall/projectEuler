# The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

def main():
    with open('large_number.txt', mode='r') as file:
        large_number_string: str = file.read()

    largest_product: int = 0
    number_of_digits: int = 13

    start_index: int = 0
    end_index: int = (start_index + number_of_digits) - 1

    while end_index < len(large_number_string):
        product: int = int(large_number_string[start_index])

        temp_index = start_index + 1

        while temp_index <= end_index:
            product *= int(large_number_string[temp_index])
            temp_index += 1

        if product > largest_product:
            largest_product = product

        start_index += 1
        end_index += 1

    print(largest_product)


if __name__ == '__main__':
    main()
