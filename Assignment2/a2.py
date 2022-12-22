import math


# problem 1
# input real
# return real


def g(x):
    if x == 0:
        return 1
    elif x != 0:
        return x+2

# problem 2
# input year 1977-1997
# return percent income or "error: year" if year
# is outside range


def f(t):
    if 1977 <= t <= 1984:
        return (2/7)*(t-1977)+12
    if 1984 < t <= 1987:
        return (t-1977)+7
    if 1987 < t <= 1997:
        return 3/5*(t-1977)+11
    else:
        return "error: year"

# problem 3
# input t years = 0
# output dollars


def h_0(t):
    costOEM = 110/((1/2)*t+1)
    return costOEM


def h_1(t):
    costNon = (((1/4)*t**2-1)**2)*26+52
    return costNon


def h(t):
    U = h_0(t)
    N = h_1(t)
    diff = U - N
    return diff

# problem 4
# input tuple (a,b,c) coefficients
# output tuple roots (x_1, x_2) where x_1 >= x_2


def q(coefficients):
    b = -coefficients[1]
    a = coefficients[0]
    c = coefficients[2]
    x1 = b + (math.sqrt((b**2) - (4*a*c)) / (2*a))
    x2 = b - (math.sqrt((b**2) - (4*a*c)) / (2*a))
    return (x1, x2)
    # problem 5
    # input [arg1,op,arg2,ans]
    # output boolean True or False


def eq(lst):
    arg1, op, arg2, ans = lst
    if op == "+":
        a = arg1 + arg2
    if op == "-":
        a = arg1 - arg2
    if op == "*":
        a = arg1 * arg2
    if op == "/":
        a = arg1 / arg2
    if a == ans:
        return True
    else:
        return False

    # problem 6
    # input list of swithes
    # output True if path from start to end


def path(lst):
    for x in lst:
        if lst[0] == 1:
            if lst[2] == 1:
                return True
        if lst[1] == 1:
            if lst[3] == 1:
                return True
            if lst[4] == 1:
                return True
        else:
            return False

# problem 7
# INPUT two numbers
# RETURN maximum of the two
# You cannot use Python's max function
# You must use if, elif, else (or some combination)


def max2d(x, y):
    if x > y:
        return x
    else:
        return y

# INPUT 3 numbers
# RETURN maximum of the three
# You must use your max2D function


def max3d(x, y, z):
    f = max2d(x, y)
    if z > f:
        return z
    else:
        return f

    # PROBLEM 8
    # INPUT dimension x and area A
    # OUTPUT length of fence


def f_(x, A):
    amount_fence = 2*x+2*A/x
    return amount_fence

# INPUT x dimension and length of fence
# OUTPUT y dimension


def g_(x, length_of_fence):
    otherSide = (length_of_fence - 2*x)/2
    return otherSide

# PROBLEM 9
# INPUT x dimension of box with 20 ft**3 volume
# OUTPUT cost in dollars


def box_cost(x):
    bcost = .3
    tcost = .2
    scost = .1
    y = 5
    side = x * y
    top_bottom = x**2
    total = (side*4)*scost + top_bottom*bcost + top_bottom*tcost
    return total

    # PROBLEM 10
    # INPUT month = 0,1,..., 11
    # OUPUT occupancy rate 0..100


def r(month):
    r = ((10/81)*month**3)-((10/3)*month**2)+((200/9)*month)+55
    return round(r)

# INPUT occupancy rate 0..100
# OUPUT Revenue generated


def R(r):
    rev = (-3/5000*r**3+9/50*r**2)*1000
    return rev


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test
    your code outside of the unit testing. Feel free to add print statements.
    You should uncomment the print statements *after* you're done testing here.
    """
    # problem 1
    # print(f"g(0) = {g(0)}")
    # print(f"g(1) = {g(1)}")
    # print(f"g(1.01) = {g(1.01)}")

    # problem 2
    # print(f"f(1976) = {f(1976)}")
    # print(f"f(1977) = {f(1977)}")
    # print(f"f(1985) = {f(1985)}")
    # print(f"f(1988) = {f(1988)}")
    # print(f"f(2000) = {f(2000)}")

    # problem 3
    # print(f"h(0) = {h(0)}")
    # print(f"h(1) = {h(1)}")
    # print(f"h(2) = {h(2)}")

    # problem 4
    # print(f"q((1,0,-1)) = {q((1,0,-1))}")
    # print(f"q((6,-1,-35)) = {q((6,-1,-35))}")
    # print(f"q((1,-7,-7)) = {q((1,-7,-7))}")

    # problem 5
    # print(eq([14, "/", 2, 7]))
    # print(eq([20, "*", 19, 381]))
    # print(eq([20, "*", 19, 380]))

    # problem 6
    # print(f"path([1,0,1,0,0]) = {path([1,0,1,0,0])}")
    # print(f"path([1,1,1,0,0]) = {path([1,1,1,0,0])}")
    # print(f"path([1,0,0,1,0]) = {path([1,0,0,1,0])}")

    # problem 7
    # print(max3d(1, 2, 3))
    # print(max3d(1, 3, 2))
    # print(max3d(3, 2, 1))

    # problem 8
    # A = 250
    # x0, x1 = 10, 20

    # length_of_fence = f_(x0, A)
    # y = g_(x0, length_of_fence)

    # print(f"{x0} x {y} ft^2 with {length_of_fence} ft of fence")

    # length_of_fence = f_(x1, A)
    # y = g_(x1, length_of_fence)
    # print(f"{x1} x {y} ft^2 with {length_of_fence} ft of fence")

    # problem 9
    # x = 2
    # print(f"cost for x = {x}ft is ${box_cost(2)}")

    # problem 10
    # january, june = 0, 5
    # print(f"Jan occupancy is {r(january)}%")
    # print(f"Jan revenue: ${R(r(january))}")

    # print(f"Jun revenue: ${R(r(june))}")
    # print(f"Jun occupancy is {r(june)}%")
