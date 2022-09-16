import math

#problem 1
#input real
#return real
def g(x):
    pass


#problem 2
#input year 1977-1997
# return percent income or "error: year" if year 
# is outside range
def f(t):
    pass


#problem 3
#input t years = 0
#output dollars
def h_0(t):
    pass

def h_1(t):
    pass 

def h(t):
    pass


#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def q(coefficients):
    pass

#problem 5
#input [arg1,op,arg2,ans]
#output boolean True or False
def eq(lst):
    pass

#problem 6
#input list of swithes
#output True if path from start to end
def path(lst):
    pass

#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
def max2d(x, y):
    pass

#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x, y, z):
    pass

#PROBLEM 8
#INPUT dimension x and area A
#OUTPUT length of fence
def f_(x, A):
    pass

#INPUT x dimension and length of fence
#OUTPUT y dimension
def g_(x, length_of_fence):
    pass

#PROBLEM 9
#INPUT x dimension of box with 20 ft**3 volume
#OUTPUT cost in dollars
def box_cost(x):
    pass

#PROBLEM 10
#INPUT month = 0,1,..., 11
#OUPUT occupancy rate 0..100
def r(month):
    pass

#INPUT occupancy rate 0..100
#OUPUT Revenue generated
def R(r):
    pass




if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing. Feel free to add print statements. 
    You should uncomment the print statements *after* you're done testing here.
    """
    #problem 1 
    # print(f"g(0) = {g(0)}")
    # print(f"g(1) = {g(1)}")
    # print(f"g(1.01) = {g(1.01)}")

    #problem 2
    # print(f"f(1976) = {f(1976)}")
    # print(f"f(1977) = {f(1977)}")
    # print(f"f(1985) = {f(1985)}")
    # print(f"f(1988) = {f(1988)}")
    # print(f"f(2000) = {f(2000)}")

    #problem 3
    # print(f"h(0) = {h(0)}")
    # print(f"h(1) = {h(1)}")
    # print(f"h(2) = {h(2)}")

    #problem 4
    # print(f"q((1,0,-1)) = {q((1,0,-1))}")
    # print(f"q((6,-1,-35)) = {q((6,-1,-35))}")
    # print(f"q((1,-7,-7)) = {q((1,-7,-7))}")

    #problem 5
    # print(eq([14, "/",2, 7]))
    # print(eq([20, "*",19, 381]))
    # print(eq([20, "*",19, 380]))

    #problem 6
    # print(f"path([1,0,1,0,0]) = {path([1,0,1,0,0])}")
    # print(f"path([1,1,1,0,0]) = {path([1,1,1,0,0])}")
    # print(f"path([1,0,0,1,0]) = {path([1,0,0,1,0])}")

    #problem 7
    # print(max3d(1,2,3))
    # print(max3d(1,3,2))
    # print(max3d(3,2,1))

    #problem 8
    # A = 250  
    # x0,x1 = 10,20

    # length_of_fence = f_(x0,A)
    # y = g_(x0,length_of_fence)

    # print(f"{x0} x {y} ft^2 with {length_of_fence} ft of fence")

    # length_of_fence = f_(x1,A)
    # y = g_(x1,length_of_fence)
    # print(f"{x1} x {y} ft^2 with {length_of_fence} ft of fence")

    #problem 9
    # x = 2
    # print(f"cost for x = {x}ft is ${box_cost(2)}")

    #problem 10
    # january,june = 0,5
    # print(f"Jan occupancy is {r(january)}%")
    # print(f"Jan revenue: ${R(r(january))}")

    # print(f"Jun occupancy is {r(june)}%")
    # print(f"Jun revenue: ${R(r(june))}")