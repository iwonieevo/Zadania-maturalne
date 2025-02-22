# https://arkusze.pl/maturalne/informatyka-2022-maj-matura-rozszerzona-2.pdf

with open("liczby.txt", "r") as f:
    numbers = [int(_) for _ in f.readlines()]

counter1, number1 = 0, None
max_total_divs, max_diff_divs = [0, 0], [0, 0]
for number in numbers:
    if str(number)[0] == str(number)[-1]:
        counter1 += 1
        if counter1 == 1:
            number1 = number
    total_div_c, diff_div_c, previous_divs, temp, div = 0, 0, [], number, 2
    while temp > 1:
        while temp % div == 0:
            if div not in previous_divs:
                diff_div_c += 1
                previous_divs.append(div)
            total_div_c += 1
            temp /= div
        div += 1
    if total_div_c > max_total_divs[1]:
        max_total_divs = [number, total_div_c]
    if diff_div_c > max_diff_divs[1]:
        max_diff_divs = [number, diff_div_c]

triples = open("trojki.txt", "w")
counter2, counter3 = 0, 0
for x in numbers:
    for y in numbers:
        for z in numbers:
            if y % x == 0 and z % y == 0 and x != y != z:
                triples.write(f"{x} {y} {z}\n")
                counter2 += 1
                for u in numbers:
                    for w in numbers:
                        if u % z == 0 and w % u == 0 and x != y != z != u != w:
                            counter3 += 1


with open("wyniki4.txt", "w") as f:
    f.write(f"4.1\nLiczb z pierwsza cyfra rowna ostatniej: {counter1}\nPierwsza taka liczba: {number1}")
    f.write(f"\n\n4.2\nNajwiecej czynnikow: {max_total_divs[1]} dla {max_total_divs[0]}\nNajwiecej roznych: {max_diff_divs[1]} dla {max_diff_divs[0]}")
    f.write(f"\n\n4.3\na){counter2}\nb){counter3}")
triples.close()
