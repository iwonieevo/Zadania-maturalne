def is_prime_number(a):
    if a == 2:
        return True
    if a % 2 == 0 or a < 2:
        return False
    for divisor in range(3, int(a ** 0.5) + 1, 2):
        if a % divisor == 0:
            return False
    return True


N, c, p1, p2 = input("Podaj liczbe do sprawdzenia: ").rstrip(), 0, "", ""

for digit in N:
    if c % 2 == 0:
        p1 += digit
    else:
        p2 += digit
    c += 1

if is_prime_number(int(p1)) and is_prime_number(int(p2)):
    print("TAK")
else:
    print("NIE")
