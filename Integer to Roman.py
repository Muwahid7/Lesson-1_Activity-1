class Roman:
    def __init__(self, number=0):
        self.number = number
    def integer_to_roman(self):
        values  = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD","C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]
        num = self.number
        roman = ""
        i = 0
        while num > 0:
            while num >= values[i]:
                roman += symbols[i]
                num -= values[i]
            i += 1
        return roman
n = int(input("Enter an integer: "))
obj = Roman(n)
print("Roman numeral:", obj.integer_to_roman())