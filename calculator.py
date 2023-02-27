from math import sqrt


class HardPassword:
    def __init__(self, default_pwd, terms):
        self.default_pwd = default_pwd
        self.terms = terms

    # gets a number and turn into a positive number
    @staticmethod
    def positive(num):
        # the number goes to the second power then we take his square root, giving the positive number if the number
        # was negative or positive
        num = num * num
        num = sqrt(num)
        return int(num)

    # gets a number and turn into a letter
    def letters(self, num):
        # library with the alphabet letters
        alphabet = ["-", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                    "t", "u", "v", "x", "w", "y", "z"]

        if num < 0:  # if the number is negative he turns the number into positive
            num = HardPassword(self.default_pwd, self.terms).positive(num)

        while num > 26:  # if the number is higher then 26 it will loop to get a number that is between 26 and 0
            num -= 26

        # now that we have a number that fits the amount of letters we get a letter
        let = alphabet[num]
        return let

    # gets a number and turn into a character
    def chars(self, num):
        # library with the possible characters
        specials = [")", '!', "@", "#", "$", "%", "¨", "&", "*", "(", ")"]

        if num < 0:  # if the number is negative he turns the number into positive
            num = HardPassword(self.default_pwd, self.terms).positive(num)

        # gives a character to a number
        while num > 10:  # if the number is higher then 10 it will loop to get a number that is between 10 and 0
            num -= 10

        char = specials[num]
        return char

    # get a number password, a function to encode it and encodes the password
    @staticmethod
    def func(default_pwd, terms):
        func_pwd = []

        # encode the number puting as the variable in the second degree function
        for pwd_num in default_pwd:
            x = pwd_num
            y = terms[0] * x ** 2 + terms[1] * x ** 1 + terms[2] * x ** 0
            func_pwd.append(int(y))
        return func_pwd

    # gets the encoded password and turns numbers into letters, upper case letters and characters
    def pwd(self, func_pwd):
        i = 0
        new_pwd = ''
        password_i = 0

        for x in func_pwd:  # loops the type of number encoding
            if i == 0:
                password_i = HardPassword(self.default_pwd, self.terms).positive(x)  # gives a number to the password
            elif i == 1:
                password_i = HardPassword(self.default_pwd, self.terms).chars(x)  # gives a character to the password
            elif i == 2:
                # gives an upper case letter to the password
                password_i = HardPassword(self.default_pwd, self.terms).letters(x).upper()
            elif i == 3:
                password_i = HardPassword(self.default_pwd, self.terms).letters(x)  # gives a letter to the password

            new_pwd += str(password_i)  # generates the password string

            i += 1  # looper index
            if i > 3:
                i = 0

        return new_pwd

    # it's the function that does all the process above and return the hard encoded password
    def create_pwd(self):
        function_password = HardPassword(self.default_pwd, self.terms).func(self.default_pwd, self.terms)
        created_password = HardPassword(self.default_pwd, self.terms).pwd(function_password)
        return print(created_password)
