import numberOperations


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def setter(self):
        self.numerator = input("Numerator: ")
        self.denominator = input("Denominator: ")

    def getter(self):
        if self.numerator == 0:
            return "0"
        if self.denominator == 0:
            self.numerator = 0
            return "Denominator cannot be equal 0!"
        return str(self.numerator) + "/" + str(self.denominator)

    def reducing(self):
        r = numberOperations.nwd(abs(self.numerator), abs(self.denominator))
        self.numerator = int(self.numerator/r)
        self.denominator = int(self.denominator/r)

    def __add__(self, other):
        den = numberOperations.nww(abs(self.denominator), abs(other.denominator))
        f = int(den / self.denominator)
        s = int(den / other.denominator)
        num_f = f * self.numerator
        num_s = s * other.numerator
        num = num_f + num_s
        result = Fraction(num, den)
        result.reducing()
        return result

    def __sub__(self, other):
        den = numberOperations.nww(abs(self.denominator), abs(other.denominator))
        f = int(den / self.denominator)
        s = int(den / other.denominator)
        num_f = f * self.numerator
        num_s = s * other.numerator
        num = num_f - num_s
        result = Fraction(num, den)
        result.reducing()
        return result

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        result = Fraction(num, den)
        result.reducing()
        return result

    def __truediv__(self, other):
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        result = Fraction(num, den)
        result.reducing()
        return result


if __name__ == '__main__':
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    print(f"a = {a.getter()}")
    print(f"b = {b.getter()}")
    print(f"a * b = {(a * b).getter()}")
    print(f"a / b = {(a / b).getter()}")
    print(f"a + b = {(a + b).getter()}")
    print(f"a - b = {(a - b).getter()}")
