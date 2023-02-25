from math import sqrt


def positive(num):
    num = num*num
    num = sqrt(num)
    return int(num)


def letters(num):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "x", "w", "y", "z"]

    if num < 0:
        num = positive(num)

    while num > 26:
        num -= 26

    if num - 1 == 0:
        let = "-"

    let = alphabet[num-1]
    return let


def chars(num):
    specials = [")", '!', "@", "#", "$", "%", "¨", "&", "*", "("]

    if num < 0:
        num = positive(num)

    if num > 10:
        char = "-"
        return char

    if num == 10:
        num = 0

    char = specials[num]
    return char


def pwd(func_pwd):
    i = 0
    new_pwd = ''

    for num in func_pwd:
        if i == 0:
            pwdi = num
        elif i == 1:
            pwdi = chars(num)
        elif i == 2:
            pwdi = letters(num).upper()
        elif i == 3:
            pwdi = letters(num)

        new_pwd += str(pwdi)

        i += 1
        if i > 3:
            i = 0

    return new_pwd


def func(default_pwd, terms):
    func_pwd = []

    for pwd_num in default_pwd:
        x = pwd_num
        y = terms[0] * x ** 2 + terms[1] * x ** 1 + terms[2] * x ** 0
        func_pwd.append(y)
    return func_pwd


default_password = [1, 4, 7, 5, 2, 8, 2, 1, 1, 1, 2, 0, 0, 0, 0, 3, 1, 1, 1, 9, 7, 5]
function1 = [1, 0, -2]
function2 = [0, 1, -8]
function3 = [0, 1, -3]
function4 = [1, 0, 0]
function5 = [0, 1, -1]
function6 = [0, 1, 0]
function7 = [1, 0, -2]
function8 = [0, 3, -1]

pwd_funcion_1 = func(default_password, function1)
pwd_funcion_2 = func(default_password, function2)
pwd_funcion_3 = func(default_password, function3)
pwd_funcion_4 = func(default_password, function4)
pwd_funcion_5 = func(default_password, function5)
pwd_funcion_6 = func(default_password, function6)
pwd_funcion_7 = func(default_password, function7)
pwd_funcion_8 = func(default_password, function8)

print(pwd(pwd_funcion_1))
print(pwd(pwd_funcion_2))
print(pwd(pwd_funcion_3))
print(pwd(pwd_funcion_4))
print(pwd(pwd_funcion_5))
print(pwd(pwd_funcion_6))
print(pwd(pwd_funcion_7))
print(pwd(pwd_funcion_8))