import math

#problem 1
#input real
#return real
def g(x):
    if x != 0:
        return x + 2
    else:
        return 1


#problem 2
#input year 1977-1997
#return percent income or "error: year" if year 
#is outside range
lst = [1977,1997]
def f(t):
    for i in range(0,len(lst)):
        if 1977 < i <= 1984:
            return 2/7 * (t - 1977) + 12
        elif 1984 < t <= 1977:
            return (t - 1977) + 7
        elif 1987 < t < 1997:
             return 3/5 * (t - 1977) + 11
        else:
            return "error:year"


#problem 3
#input t years = 0
#output dollars
lst == [0, 1, 2]
def h_0(t):
    for t[h_0] in lst: 
        if t == 0:
            return 110 / (1/2) * t + 1
        else:
            if t!= 0:
                return 26 * ((1/4) * t**2 - 1) ** 2 + 52
def h_1(t):
    for t[h_1] in lst:
        if t == 0: 
            return 110 / (1/2) * t + 1
        else:
            if t!= 0:
                return 26 * ((1/4) * t**2 - 1) ** 2 + 52

def h(t):    
    return abs(h_0(t)-(h_1(t)))

 


#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def q(coefficients):
    import math
    

#problem 5
#input [arg1,op,arg2,ans]
#output arg1 op arg2 == ans

def eq(lst):
    for item in lst:
     if item[0] * item[2] >= item[3]:
        return True
    else:
        return False


#problem 6
#input list of swithes
#output True if path from start to end
def path(lst):
    s0, s1, s2, s3, s4 = lst

    # s0 is required for any path
    if not s0:
        c = False
    # s0 + s2 == complete path
    elif s2:
        c = True
    # ((s0 + s1 + s3) OR (s0 + s1 + s4)) == complete path
    elif s1 and (s3 or s4):
        c = True
    return c


#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
def max2d(x,y):
    if x > y:
        return x
    else:
        return y

#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x,y,z):
    print(max2d(x, max2d(y,z)))

#from homework
def m(x,y):
    return (x > y)*x + (x <= y)*y

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

    pass