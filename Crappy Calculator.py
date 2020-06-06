from math import sqrt, sin, cos, tan, log


def plus(x, y):
    try:
        return x + y
    except Exception:
        return "Enter numerical values, please"


def minus(x, y):
    try:
        return x - y
    except Exception:
        return "Enter numerical values, please"


def times(x, y):
    try:
        return x * y
    except Exception:
        return "Enter numerical values, please"


def dividedby(x, y):
    try:
        return x * y
    except Exception:
        return "Enter numerical values, please"


def solveforquad(a, b, c):
    try:
        zero = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
        otherzero = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
        if type(zero) == float:
            return zero
        if type(otherzero) == float:
            return otherzero
    except Exception:
        return "Enter real numbers for a, b, and c"


def tothepowerof(a, b):
    try:
        return a ** b
    except Exception:
        return "Enter real numbers, please"


def squareroot(square):
    try:
        return sqrt(square)
    except Exception:
        return "Enter real numbers, please"


def cosine(x):
    try:
        return cos(x)
    except Exception:
        return "Enter a real number, please"


def sine(x):
    try:
        return sin(x)
    except Exception:
        return "Enter a real number, please"


def tanget(x):
    try:
        return tan(x)
    except  Exception:
        return "Enter a real number, please"


def logarithim(x, y):
    try:
        return log(x, y)
    except Exception:
        return "Enter real numbers, please"


def meanof(list):
    try:
        return sum(list) / len(list)
    except Exception:
        return "Data must be a list composed of real numbers"


def modeof(x):
    try:
        modedict = dict()
        for i in x:
            modedict[i] = modedict.get(i, 0) + 1
        numcount = -1
        for j in modedict:
            if modedict[j] > numcount:
                numcount = modedict[j]
                moad = j
        return moad
    except Exception:
        return "Data must be in a list"


def medianof(list):
    try:
        sorted(list)
        if len(list) % 2 != 0:
            return list[len(list) // 2]
        else:
            return meanof((list[len(list) / 2]), (list[len(list) / 2 - 1]))
    except Exception:
        print("Data must be a list composed of real numbers")


x = [11, 2, 4, 7, 2, 6, 3, 5, 4, 2, 3, 4, 4, 5, 6, 7, 5, 3, 3, 2, 4, 4, 56, 6, 5, 4, 3, 2, 4, 5, 6, 7, 8]
print(solveforquad(1,-6,9))
