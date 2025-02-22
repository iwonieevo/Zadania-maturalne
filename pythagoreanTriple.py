from math import sqrt


def main():
    x, y = int(input("Input first number: ")), int(input("Input second number: "))
    z1, z2 = sqrt(x**2 + y**2), sqrt(max(x, y)**2 - min(x, y)**2)
    if not z1 == float(int(z1)): z1 = 0
    if not z2 == float(int(z2)): z2 = 0

    if not z1 == 0: print(f"{int(sorted([x, y, z1])[0])}, {int(sorted([x, y, z1])[1])}, {int(sorted([x, y, z1])[2])}")
    if not z2 == 0: print(f"{int(sorted([x, y, z2])[0])}, {int(sorted([x, y, z2])[1])}, {int(sorted([x, y, z2])[2])}")
    if z1 == 0 and z2 == 0: print(0)


if __name__ == "__main__":
    main()
