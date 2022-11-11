import math 
#PROBLEM 1
#INPUT a function f(x)
#RETURN a function lambda x: (f(x+h) - f(x-h))/(2h)
# where h = .00001
# Note, in this function we are not returning a numeric value, but a lambda function.
def D(f):
    pass

#INPUT function of single variable x, starting point x, precision tau
#OUTPUT a root of f
def newton(f,x,tau):
    pass


#Problem 2
#INPUT a number
#RETURN -1 if number is <= 0, 1 otherwise
def sign(x):
    pass

#INPUT function, interval(a, b), tau
#RETURN root
def bisection(f,a,b,tau):
    pass


#Problem 3
#INPUT function, two starting values (x0 and x1) and tau
#RETURN root
def secant(f,x0,x1,tau):
    pass

#Problem 4
#INPUT function, start a, end b, divisions
#RETURN area
def simpson(f,a,b,n):
    pass

#Problem 5
#INPUT list of objects
#RETURN list of permutations
def permutation(lst):
    pass

#Problem 6
#INPUT class 
#RETURN method reduce(self) completed to reduce fraction
class fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()
    def get_numerator(self):
        return self.numerator
    def get_denominator(self):
        return self.denominator
    def reduce(self):
        pass 
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

if __name__ == "__main__":
   ''' uncomment if needed'''
#   Problem 1
#    p1 = [[lambda x:x**2 - 2, 100],[lambda x:x**6-x-1,1.5],
#          [lambda x:x**3-(100*(x**2))-x + 100,0]]
#    tau = 0.0001

#    for f,g in p1:
#        root = newton(f,g,tau)
#        print(root,f(root))

#    Problem 2
#    print(bisection(lambda x:x**3-x-2,1.0,2.0,0.0001))
#    print(bisection(lambda x:x**6-x-1,1.0,2.0,.0001))

#    Problem 3
#    print(secant(lambda x:x**6-x-1,2.0,1.0,.0001))
#    print(secant(lambda x:x**3-x-2,1.0,2.0,0.0001))
   
#    Problem 4
#    print(simpson(lambda x: 3*(x**2)+1,0,6,2))
#    print(simpson(lambda x: (x**2),0,5,6))
#    print(simpson(lambda x: 1/x,1,11,6))
#    print(simpson(lambda x: math.sin(x),0,math.pi,10))

#    Problem 5
#    print(permutation([1,2,3]))
#    print(permutation([1,2,3,4]))

#    Problem 6
# x = fraction(2*3*4,4*3*5)
# y = fraction(2*7,7*2)
# z = fraction(13,14)
# a = fraction(13*2*7,14)
# print(x)
# print(y)
# print(z)
# print(a)