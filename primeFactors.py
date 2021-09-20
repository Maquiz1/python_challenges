# WRITE A PYTHON FUNCTION TO FIND ALL PRIME FACTORS
# INPUT: INTEGER VALUE
# OUTPUT: LIST OF PRIME FACTORS

def get_prime_factors(N):
    factors = list()
    divisor = 2
    while divisor < N:
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N / divisor

        else:
            divisor += 1
    return factors


print(get_prime_factors(100))
