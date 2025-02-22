# https://arkusze.pl/maturalne/informatyka-2021-maj-matura-rozszerzona-2.pdf

import string as s

data = open("instrukcje.txt", "r").readlines()
answer = open("wyniki4.txt", "w")
instructions = [x.replace("\n", "").split(" ") for x in data]
finalWord = ""
maxL = 0
currentL = 0
maxS = ""
prev = ""
countLetters = {}
for instruction in instructions:
    if prev == instruction[0]: currentL += 1
    else:
        if currentL > maxL:
            maxL = currentL
            maxS = prev
        currentL = 1
    prev = instruction[0]
    if instruction[0] == 'DOPISZ':
        finalWord += instruction[1]
        if countLetters.__contains__(instruction[1]): countLetters[instruction[1]] += 1
        else: countLetters[instruction[1]] = 1
    elif instruction[0] == 'ZMIEN':
        finalWord = list(finalWord)
        finalWord[-1] = instruction[1]
        finalWord = "".join(finalWord)
    elif instruction[0] == 'USUN':
        finalWord = list(finalWord)
        finalWord.pop()
        finalWord = "".join(finalWord)
    elif instruction[0] == 'PRZESUN':
        finalWord = list(finalWord)
        if instruction[1] != "Z": finalWord[finalWord.index(instruction[1])] = s.ascii_uppercase[s.ascii_uppercase.index(instruction[1]) + 1]
        else: finalWord[finalWord.index(instruction[1])] = "A"
        finalWord = "".join(finalWord)

mostCommonLetter = list(reversed(sorted(countLetters.items(), key=lambda item: item[1])))[0]
answer.write("4.1\n{}\n\n4.2\n{} {}\n\n4.3\n{} {}\n\n4.4\n{}".format(len(finalWord), maxS, maxL, mostCommonLetter[0], mostCommonLetter[1], finalWord))
