from math import sqrt


class HardPassword:
    def __init__(self, default_pwd, terms):
        self.default_pwd = default_pwd
        self.terms = terms

    @staticmethod
    def positive(num):
        num = num*num
        num = sqrt(num)
        return int(num)

    def letters(self, num):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "x", "w", "y", "z"]

        if num < 0:
            num = HardPassword(self.default_pwd, self.terms).positive(num)

        while num > 26:
            num -= 26

        if num - 1 == 0:
            let = "-"

        let = alphabet[num-1]
        return let

    def chars(self, num):
        specials = [")", '!', "@", "#", "$", "%", "¨", "&", "*", "("]

        if num < 0:
            num = HardPassword(self.default_pwd, self.terms).positive(num)

        if num > 10:
            char = "-"
            return char

        if num == 10:
            num = 0

        char = specials[num]
        return char

    @staticmethod
    def func(default_pwd, terms):
        func_pwd = []

        for pwd_num in default_pwd:
            x = pwd_num
            y = terms[0] * x ** 2 + terms[1] * x ** 1 + terms[2] * x ** 0
            func_pwd.append(y)
        return func_pwd

    def pwd(self, func_pwd):
        i = 0
        new_pwd = ''
        password_i = 0

        for x in func_pwd:
            if i == 0:
                password_i = x
            elif i == 1:
                password_i = HardPassword(self.default_pwd, self.terms).chars(x)
            elif i == 2:
                password_i = HardPassword(self.default_pwd, self.terms).letters(x).upper()
            elif i == 3:
                password_i = HardPassword(self.default_pwd, self.terms).letters(x)

            new_pwd += str(password_i)

            i += 1
            if i > 3:
                i = 0

        return new_pwd

    def create_pwd(self):
        function_password = HardPassword(self.default_pwd, self.terms).func(self.default_pwd, self.terms)
        created_password = HardPassword(self.default_pwd, self.terms).pwd(function_password)
        return print(created_password)


default_password = [1, 4, 7, 5, 2, 8, 2, 1, 1, 1, 2, 0, 0, 0, 0, 3, 1, 1, 1, 9, 7, 5]
function1 = [1, 0, -2]
function2 = [0, 1, -8]
function3 = [0, 1, -3]
function4 = [1, 0, 0]
function5 = [0, 1, -1]
function6 = [0, 1, 0]
function7 = [1, 0, -2]
function8 = [0, 3, -1]

password1 = HardPassword(default_password, function1)
password2 = HardPassword(default_password, function2)
password3 = HardPassword(default_password, function3)
password4 = HardPassword(default_password, function4)
password5 = HardPassword(default_password, function5)
password6 = HardPassword(default_password, function6)
password7 = HardPassword(default_password, function7)
password8 = HardPassword(default_password, function8)

password1.create_pwd()
password2.create_pwd()
password3.create_pwd()
password4.create_pwd()
password5.create_pwd()
password6.create_pwd()
password7.create_pwd()
password8.create_pwd()
