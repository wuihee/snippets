def naive_prime(num):
    factors = []

    for i in range(2, int(num ** 0.5)):
        while num % i == 0:
            factors.append(i)
            num //= i

    return factors


if __name__ == "__main__":
    dividend = int(input("Enter a number to be factorized: "))
    factors = naive_prime(dividend)
    print(factors)
