def sieve_of_Eratosthenes(bound):
    primes = []
    is_prime = [True] * (bound + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= bound:
        if is_prime[p]:
            for i in range (p * p, bound + 1, p):
                is_prime[i] = False
        p += 1

    for p in range(2, bound + 1):
        if is_prime[p]:
            primes.append(p)

    return primes

n = int(input("Enter the number up to which you want to check the primes of: "))
primes = sieve_of_Eratosthenes(n)
prime_string = ", ".join(map(str, primes))
print("The prime numbers smaller than or equal to", n, "are:", prime_string)