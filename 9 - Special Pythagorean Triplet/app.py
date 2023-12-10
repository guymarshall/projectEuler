# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#   a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def main():
    pythagorean_triplets: list = []

    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                is_pythagorean_triplet: bool = (a ** 2) + (b ** 2) == (c ** 2)

                if is_pythagorean_triplet:
                    total = a + b + c

                    if total == 1000:
                        print(a * b * c)


if __name__ == '__main__':
    main()
