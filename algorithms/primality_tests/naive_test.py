def is_prime(num):
    """Checks if num is prime."""
    return num > 1 and not any(num % n == 0 for n in range(2, num))


if __name__ == "__main__":
    print(is_prime(11))
    print(is_prime(102))
