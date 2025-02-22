def is_prime_number(a):
    if a == 2:
        return True
    if a % 2 == 0 or a <= 1:
        return False

    prime = int(a ** 0.5) + 1
    for divisor in range(3, prime, 2):
        if a % divisor == 0:
            return False
    return True


def nwd(b, c):
    ret = 1
    for i in range(1, b + 1):
        if is_prime_number(i) and b % i == 0 and c % i == 0:
            ret *= i
    return ret


def nww(d, e):
    return d * e/nwd(d, e)




