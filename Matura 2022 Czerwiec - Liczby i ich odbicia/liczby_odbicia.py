# https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona-2.pdf

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True


data = open("liczby.txt", "r").readlines()
answer = open("wyniki4.txt", "w")
answer.write("4.1\n")
maxDiff = 0
rememberNumber = ""
primes = []
uniqueNumbers = []
for i in range(len(data)):
    data[i] = data[i].replace("\n", "")
    realNumber = ""
    for d in list(reversed(data[i])):
        realNumber += d
    if int(realNumber) % 17 == 0:
        answer.write(realNumber + "\n")
    oldMaxDiff = maxDiff
    maxDiff = max(maxDiff, (abs(int(data[i]) - int(realNumber))))
    if oldMaxDiff != maxDiff:
        rememberNumber = data[i]
    if is_prime(int(data[i])) and is_prime(int(realNumber)):
        primes.append(data[i])
    if uniqueNumbers.count(data[i]) == 0:
        uniqueNumbers.append(data[i])


answer.write("\n4.2\n{}\t{}\n".format(rememberNumber, maxDiff))
answer.write("\n4.3\n")
for prime in primes:
    answer.write(prime + "\n")
answer.write("\n4.4\n")
counterOfDoubles = 0
counterOfTriples = 0
for number in uniqueNumbers:
    if data.count(number) == 2:
        counterOfDoubles += 1
    if data.count(number) == 3:
        counterOfTriples += 1
answer.write("{}\t{}\t{}\t".format(len(uniqueNumbers), counterOfDoubles, counterOfTriples))
