import math

#Problem 1

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    pass

#INPUT t days
#RETURN number of teeth
def N_t(t):
    pass

#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    pass


#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    pass

###########################################################################
# Function for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN True if discriminant is real, False otherwise
def q(t):
    pass


###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT item and list
#RETURN True if item is in the list
#CONSTRAINT You cannot use 'in' -- must use bounded looping.
def m(x,lst):
    pass

def amt(r,no_tax):
    pass

###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT p0 = (x0,y0) p1 = (x1,y1)
#RETURN (m, b) for line y = mx + b
def f(p0, p1):
    pass


###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

# Use these error messages according to the case that you encounter.
# You can use them err_msg[0] or err_msg[1].
# Make sure that you don't change the error messages. 
# Use them as such without alterations.
err_msg = ["Data Error: 0 values", "Data Error: 0 in data"]

def arithmetic_mean(nlst):
    pass

def geo_mean(nlst):
    pass

def har_mean(nlst):
    pass

def RMS_mean(nlst):
    pass

###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT x filters
#RETURN fixed cost
def F(x):
    pass

#INPUT x filters
#RETURN variable cost
def V(x):
    pass

#INPUT x filters
#RETURN total cost
def C(x):
    pass



###########################################################################
# Functions for Problem 7
###########################################################################

#INPUT list [p,i,n] principal, interest rate, number of years
#RETURN monthly payment amount
def Mortgage(house):
    pass


#INPUT list [p,i,n] principal, interest rate, number of years
#RETURN the difference between total paid and actual value of home
#REQUIRES Use Mortgage function
def total_paid(house):
    pass


###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT first two members of geometric series and list size
#RETURN returns a list of geometric series of list size
def geo(lst, n):
    pass

###########################################################################
# Functions for Problem 9
###########################################################################
# A
#INPUT first two members of geometric series and list size
#RETURN returns a list of geometric series of list size
def two_min(lst):
    pass

###########################################################################
# B
#INPUT list of numbers
#RETURN A list of the maximum and number of times it appears or empty list
def mm(lst):
    pass
###########################################################################
# C
#INPUT list of numbers
#RETURN true if list is monotonic, false otherwise
def mo(lst):
    pass

###########################################################################
# D
#INPUT list of weights and weight
#RETURN the list of weights greater than or equal 
def w(classes, wt):
    pass

###########################################################################
# F
#INPUT two tuples represeting the points
#RETURN the distance between the points 
def dis(p0, p1):
    pass

###########################################################################
# G
#INPUT list of points (point is represented by a tuple)
#RETURN Total distance
def trip(lst):
    pass   

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please uncomment the print statements below. You are encouraged to
    write some of your own tests here or in the a3_test.py file.

    Remember to comment the print statements below after you are done 
    testing.
    """
    
    # #problem 1
    # print(N(500,100,4)) 
    # print(N_t(1000))
    # print(W(10,1))
    # print(L(33.8,512,0.515))

    #problem 2
    # print(q((1,4,-21)))
    # print(q((3,6,10)))
    # print(q((1,0,-4)))

    #problem 3
    # receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
    # no_tax = [33,5,2]
    # print(amt(receipt,no_tax))

    # #problem 4
    # print(f((2,3),(6,4)))
    # print(f((1,6),(3,2)))
    # print(f((1,3),(1,5)))
 
    #problem 5
    # print(arithmetic_mean([1,2,3]))
    # print(geo_mean([2,4,8]))
    # print(har_mean([1,2,3]))
    # print(RMS_mean([1,3,4,5,7]))

    #problem 6
    # print(C(0))
    # print(C(100))
    # print(C(1000))

    #problem 7
    # house = [300000,2.9,30]
    # print(Mortgage(house))
    # print(total_paid(house))

    # #problem 8
    # data = [[1,-3],[2,6],[10,5],[math.sqrt(2),-math.sqrt(2)]]
    # for d in data:
    #     print(geo(d,4))

    # #problem 9

    #A
    # data = [[5,4,3,2,1],[1,2],[1,4,2,0,1,100],[5,0,0,5],[1,2,3,4,5]]
    # for d in data:
    #     print(f"{two_min(d)}")

    #B
    #data = [[],[1],[2,1,2,1,2],[0,1,100],[1,2,3,1,2,3,3,5]]
    # for d in data:
    #     print(f"{d} {mm(d)}")

    #C 
    # data = [[1],[1,1.1,1.1,1.3,2],[20,21,22,23,22,24],[1,10],[10,1]]
    # for d in data:
    #     print(f"{mo(d)}")

    #D
    # classes = [125,133,141,149,157,165,174,184,197,"HW"]
    # wts = [110,163,166,184,197,198]
    # for w_ in wts:
    #     print(f"{w(classes,w_)}")

    #E
    # data = [[(1,2,3,1),(4,2,3,2)],[(1,2),(3,1)],[(3,),(2,)]]
    # for p0,p1 in data:
    #     print(f"{dis(p0,p1)}") 

    #F
    #data = [[(1,),(3,),(7,)],[(1,1)],[(0,0),(1,0),(1,1),(1,2)],[(0,0,0),(1,1,1)]]
    # for d in data:
    #     print(f"{trip(d)}")
