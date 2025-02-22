# https://zadania.dlamaturzysty.info/s/5159/81431-informatyka/5040155-zadania-z-informatyki-Tworzenie-algorytmow.htm?podstr=3

def quick_raising_to_power(x, k_bin_repr):
    result = x
    for i in k_bin_repr[1:]:
        result *= result
        if int(i):
            result *= x
    return result


# tak naprawde n i binarna reprezentacja k sa zbedne - wystaczyloby x i k; przyklad takiego usprawnionego algorytmu:

def better_quick_raising_to_power(x, k):
    result = x
    for i in bin(k)[3:]:
        result *= result
        if int(i):
            result *= x
    return result


# podpunkt 2

for j in [4, 5, 6, 7, 8, 15, 16, 22, 32]:
    print(f"k = {j}, reprezentacja binarna k = {bin(j)[2:]}, liczba mnozen = {len(bin(j)[3:]) + bin(j)[3:].count('1')}")


print(quick_raising_to_power(int(input("x = ")), input("k in binary = ")))
