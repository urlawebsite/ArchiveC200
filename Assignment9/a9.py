import math
# PROBLEM 1


def D(f):

    def df(x):
        h = 0.00001
        return (f(x+h) - f(x-h))/(2*h)
    return df


def newton(f, x, tau):
    while abs(f(x)) > tau:
        x = x - f(x)/D(f)(x)
    return x

# Problem 2
# INPUT a number
# RETURN -1 if number is <= 0, 1 otherwise


def sign(x):
    if x <= 0:
        return -1
    else:
        return 1

# INPUT function, interval(a, b), tau
# RETURN root


def bisection(f, a, b, tau):
    c = (a+b)/2
    d = b-c
    if d <= tau:
        return c
    elif sign(f(a)) == sign(f(c)):
        a = c
        return bisection(f, a, b, tau)
    else:
        b = c
        return bisection(f, a, b, tau)

    # Problem 3
    # INPUT function, two starting values (x0 and x1) and tau
    # RETURN root


def secant(f, x0, x1, tau):
    sum = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    x2 = sum
    if abs(f(sum)) > tau:
        ans = (secant(f, x1, x2, tau))
    else:
        ans = x2
    return ans


# Problem 4
# INPUT function, start a, end b, division
# RETURN area


def simpson(f, a, b, n):
    delta_x = (b-a)/n
    x_0 = a
    sum = 0
    for i in range(0, n+1):
        if i == 0 or i == n:
            sum += f(x_0 + i*delta_x)
        elif i % 2 == 0:
            sum += 2*f(x_0 + i*delta_x)
        else:
            sum += 4*f(x_0 + i*delta_x)
    return (b-a)/(3*n) * sum

    # Problem 5
    # INPUT list of objects
    # RETURN list of permutations


def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l

    # Problem 6
    # INPUT list of objects
    # RETURN list of combinations

# Problem 6
# INPUT class
# RETURN method reduce(self) completed to reduce fraction


class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def reduce(self):
        a = self.numerator
        b = self.denominator
        while b != 0:
            a, b = b, a % b
        self.numerator = self.numerator // a
        self.denominator = self.denominator // a

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


if __name__ == "__main__":
    ''' uncomment if needed'''
#   Problem 1
# p1 = [[lambda x:x**2 - 2, 100], [lambda x:x**6-x-1, 1.5],
#       [lambda x:x**3-(100*(x**2))-x + 100, 0]]
# tau = 0.0001

# for f, g in p1:
#     root = newton(f, g, tau)
#     print(root, f(root))
# print(newton(36, 200, 0.0001))


#    Problem 2
# print(bisection(lambda x: x**3-x-2, 1.0, 2.0, 0.0001))
# print(bisection(lambda x: x**6-x-1, 1.0, 2.0, .0001))

#    Problem 3
# print(secant(lambda x: x**6-x-1, 2.0, 1.0, .0001))
# print(secant(lambda x: x**3-x-2, 1.0, 2.0, 0.0001))

#    Problem 4
# print(simpson(lambda x: 3*(x**2)+1, 0, 6, 2))
# print(simpson(lambda x: (x**2), 0, 5, 6))
# print(simpson(lambda x: 1/x, 1, 11, 6))
# print(simpson(lambda x: math.sin(x), 0, math.pi, 10))

#    Problem 5
# print(permutation([1, 2, 3]))
# print(permutation([1, 2, 3, 4]))
# print(permutation([]))

# #    Problem 6
# x = fraction(2*3*4, 4*3*5)
# y = fraction(2*7, 7*2)
# z = fraction(13, 14)
# a = fraction(13*2*7, 14)
# print(x)
# print(y)
# print(z)
# print(a)
