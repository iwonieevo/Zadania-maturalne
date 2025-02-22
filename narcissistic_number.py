# https://zadania.dlamaturzysty.info/s/5159/81431-informatyka/5040155-zadania-z-informatyki-Tworzenie-algorytmow.htm?podstr=2

def narcissistic_number(x, b):
    b_base_x, temp = "", x
    while temp != 0:
        b_base_x = str(temp % b) + b_base_x
        temp = int(temp / b)
    n = len(b_base_x)
    for digit in b_base_x:
        temp += int(digit) ** n
    if temp == x:
        return True
    else:
        return False


if narcissistic_number(int(input("x = ")), int(input("B = "))):
    print("TAK")
else:
    print("NIE")
