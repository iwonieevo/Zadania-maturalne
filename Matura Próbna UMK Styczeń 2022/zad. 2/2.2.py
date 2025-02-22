primesOneDigit, primesTwoDigits, i, n, answer = [], [], 2, 99, []
numbers = [True] * (n + 1)
while i ** 2 <= n:
    if numbers[i]:
        j = i ** 2
        while j <= n:
            numbers[j] = False
            j += i
    i += 1

for i in range(2, n + 1):
    if numbers[i]:
        if i < 10:
            primesOneDigit.append(i)
        if i in range(10, 100):
            primesTwoDigits.append(i)

for x in primesTwoDigits:
    for y in primesOneDigit:
        answer.append(f"{str(x)[0]}{y}{str(x)[1]}")

print(answer)
