def comm_div(n, d):
    while n%d != 0:
        oldn = n
        oldd = d

        n = oldd
        d = oldn % oldd
    return d

class Fractie:

    def __init__(self, num, den):
        if den == 0:
            raise ValueError('Denominator can not be 0!')
        self.num = num
        self.den = den

    def __str__(self):
        print(str(self.num) + '/' + str(self.den))

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = comm_div(newnum,newden)
        return str(newnum//common) + '/' + str(newden//common)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = comm_div(newnum, newden)
        return str(newnum // common) + '/' + str(newden // common)

    def inverse(self):
            return str(self.den) + '/' + str(self.num)


f1 = Fractie(8,3)
f2 = Fractie(1,6)
print(f1.inverse())


