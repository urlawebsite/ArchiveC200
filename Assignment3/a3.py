import math
# math.exp() = e^x
# math.ceil = rounds
# math.log(x) = log_e(x) or ln(x)
"""
Things not allowed is min,max,append, while loops, and sum
"""
# Problem 1


# INPUT n0 start colony size, m growth rate, t time
# RETURN final colony size


def N(n_0, m, t):
    bactg = n_0*math.exp(m*t)
    return bactg

# INPUT t days
# RETURN number of teeth


def N_t(t):
    nteeth = 71.8*math.exp(-8.96*math.exp(-0.0685*t))
    return math.ceil(nteeth)
# INPUT pressures Pi, Pf
# RETURN work joules


def W(P_i, P_f):
    R = 8.314
    T = 300
    work = R*T*math.log(P_i/P_f)
    return math.ceil(work)
    # INPUT V miles per hour, A area, C_l lift coefficient
    # RETURN lbs


def L(V, A, C_l):
    k = 0.0033
    lift = k*(V**2)*A*C_l
    return math.ceil(lift)

###########################################################################
# Function for Problem 2
###########################################################################
# INPUT t = (a,b,c)
# RETURN True if discriminant is real, False otherwise


def q(t):
    a = t[0]
    b = t[1]
    c = t[2]
    d = a**2 - 4*b*c
    if d > 0:
        return True
    elif d == 0:
        return -b/2*a
    else:
        return False
    ###########################################################################
    # Functions for Problem 3
    # Problem 3 correction: Typo error regarding Indiana tax
    ###########################################################################
    # INPUT item and list
    # RETURN True if item is in the list
    # CONSTRAINT You cannot use 'in' -- must use bounded looping.

# create the total without tax


def m(x, lst):
    e = False
    for i in lst:
        # for j in i:
        for h in x:
            if i == h:
                print(i)


def amt(r, no_tax):
    subt = 0
    for num_lst in r:
        for item in num_lst:
            if item != no_tax:
                subt = subt + round(item * 0.07) + item
    #total = subt + m(no_tax, r)
    return subt


# print(15.7)


###########################################################################
# Functions for Problem 4
###########################################################################
# INPUT p0 = (x0,y0) p1 = (x1,y1)
# RETURN (m, b) for line y = mx + b


def f(p0, p1):
    x = p1[0]-p0[0]
    y = p1[1]-p0[1]
    if x != 0:
        m = y/x
        b = p1[1] - (m*p1[0])
        return (m, b)
    else:
        return ()

    ###########################################################################
    # Functions for Problem 5
    ###########################################################################
    # INPUT List of numbers
    # RETURN Various means or error message
    # Use these error messages according to the case that you encounter.
    # You can use them err_msg[0] or err_msg[1].
    # Make sure that you don't change the error messages.
    # Use them as such without alterations.
err_msg = ["Data Error: 0 values", "Data Error: 0 in data"]


def arithmetic_mean(nlst):
    atotal = 0
    n = len(nlst)
    if n == 0:
        return 0
    else:
        for num in nlst:
            atotal += num/n
    return atotal


def geo_mean(nlst):
    a = 10
    n = len(nlst)
    for num in nlst:
        sum = math.ceil(math.log10(num))
        gtotal = a**sum/n
    if n == 0:
        return err_msg
    return math.ceil(gtotal)


def har_mean(nlst):
    n = len(nlst)
    ftotal = 0
    for num in nlst:
        f = 1/num
        ftotal += f
        htotal = n/ftotal
    if htotal == 0:
        return err_msg

    return htotal


def RMS_mean(nlst):
    n = len(nlst)
    xtotal = 0
    for num in nlst:
        x = num**2
        xtotal += x
        sum = math.sqrt((xtotal/n))
        if sum == 0:
            return err_msg
    return sum


###########################################################################
# Functions for Problem 6
###########################################################################
# INPUT x filters
# RETURN fixed cost


def F(x):
    ans = (x**0) + 10000
    return ans
    # INPUT x filters
    # RETURN variable cost


def V(x):
    ans = (-0.001*x**2)+10*x
    return ans

# INPUT x filters
# RETURN total cost


def C(x):
    a = F(x)
    b = V(x)
    ans = (b+a)
    return ans
    ###########################################################################
    # Functions for Problem 7
    ###########################################################################

    # INPUT list [p,i,n] principal, interest rate, number of years
    # RETURN monthly payment amount


def Mortgage(house):
    a = house[1]
    b = house[2]
    c = house[3]
    num = (((b/100)/12)*(1+((b/100)/12))**(c*12))
    num2 = ((1+((b/100)/12))**(c*12)-1)
    ans = a*(num/num2)
    return round(ans, 2)

# INPUT list [p,i,n] principal, interest rate, number of years
# RETURN the difference between total paid and actual value of home
# REQUIRES Use Mortgage function


def total_paid(house):
    a = house[1]
    b = house[2]
    c = house[3]
    m = Mortgage(house)
    ans = (m*c*12)-a
    return round(ans, 2)


###########################################################################
# Functions for Problem 8
###########################################################################
# INPUT first two members of geometric series and list size
# RETURN returns a list of geometric series of list size
def geo(lst, n):
    r = lst[1]/lst[0]
    nlst = [lst[0], lst[1]]
    exp = 2
    while (len(nlst) < n):
        nlst.append(lst[0]*(r**exp))
        exp += 1
        return nlst
    ###########################################################################
    # Functions for Problem 9
    ###########################################################################
    # A
    # INPUT first two members of geometric series and list size
    # RETURN returns a list of geometric series of list size


def two_min(lst):
    v = lst[0]
    v2 = lst[1]
    for num in lst:
        if num < v:
            v = num

    for num2 in lst:
        if num2 < v2 and num2 > v:
            v2 = num2

    return v, v2
    ###########################################################################
    # B
    # INPUT list of numbers
    # RETURN A list of the maximum and number of times it appears or empty list


def mm(lst):
    max = 0
    occur = 0
    for i in lst:
        if i > max:
            max = i
    for j in lst:
        if j == occur:
            occur += 1
    value = [max, occur]
    return value
    ###########################################################################
    # C
    # INPUT list of numbers
    # RETURN true if list is monotonic, false otherwise


def mo(lst):
    for x in lst:
        for i in range(len(lst)+1):
            if x <= i:
                return True
        else:
            return False


###########################################################################
# D
# INPUT list of weights and weight
# RETURN the list of weights greater than or equal


def w(classes, wt):
    pwt = []
    classes[9] = 200
    for num in range(len(classes)):
        if wt < classes[num]:
            pwt.append(classes[num])

    for last in range(len(pwt)):
        if pwt[last] == 200:
            pwt[last] = "HW"
            return pwt
###########################################################################
# E
# INPUT two tuples represeting the points
# RETURN the distance between the points


def dis(p0, p1):
    total = 0
    lst1 = []
    lst2 = []
    lst_total = []

    for i in range(len(p0 and p1)):
        lst1.append(p0[i])
        lst2.append(p1[i])
        lst_total.append((lst1[i]-lst2[i])**2)
        total += (lst_total)
    ttotal = (total)**(1/2)
    return round(ttotal, 2)

###########################################################################
# F
# INPUT list of points (point is represented by a tuple)
# RETURN Total distance


def trip(lst):
    total = 0
    for i in range(len(lst)):
        if i == 0:
            total += 0
        else:
            total += dis(lst[i-1], lst[i])
    return total


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file,
    please uncomment the print statements below. You are encouraged to
    write some of your own tests here or in the a3_test.py file.

    Remember to comment the print statements below after you are done
    testing.
    """

# problem 1
# print(N(500, 100, 4))
# print(N_t(1000))
# print(W(10, 1))
# print(L(33.8, 512, 0.515))

# problem 2
# print(q((1, 4, -21)))
# print(q((3, 6, 10)))
# print(q((1, 0, -4)))
# print(q((2, -4, 2)))


# problem 3
receipt = [[1, 1.45], [3, 10.00], [2, 1.45], [5, 2.00]]
no_tax = [33, 5, 2]
print(m(no_tax, receipt))
#print(amt(receipt, no_tax))

# #problem 4
#print(f((2, 3), (6, 4)))
#print(f((1, 6), (3, 2)))
#print(f((1, 3), (1, 5)))

# problem 5
#print(arithmetic_mean([1, 2, 3]))
#print(geo_mean([2, 4, 8]))
#print(har_mean([1, 2, 3]))
#print(RMS_mean([1, 3, 4, 5, 7]))

# problem 6
# print(C(0))
# print(C(100))
# print(C(1000))

# problem 7
#house = [300000,2.9,30]
# print(Mortgage(house))
# print(total_paid(house))

# #problem 8
#data = [[1, -3], [2, 6], [10, 5], [math.sqrt(2), -math.sqrt(2)]]
# for d in data:
#    print(geo(d, 4))

# #problem 9

# A
# data = [[5, 4, 3, 2, 1], [1, 2], [1, 4, 2, 0, 1, 100],
#        [5, 0, 0, 5], [1, 2, 3, 4, 5]]
# for d in data:
#    print(f"{two_min(d)}")

# B
# data = [[],[1],[2,1,2,1,2],[0,1,100],[1,2,3,1,2,3,3,5]]
# for d in data:
#     print(f"{d} {mm(d)}")

# C
# data = [[1],[1,1.1,1.1,1.3,2],[20,21,22,23,22,24],[1,10],[10,1]]
# for d in data:
#     print(f"{mo(d)}")

# D
# classes = [125,133,141,149,157,165,174,184,197,"HW"]
# wts = [110,163,166,184,197,198]
# for w_ in wts:
#     print(f"{w(classes,w_)}")

# E
# data = [[(1,2,3,1),(4,2,3,2)],[(1,2),(3,1)],[(3,),(2,)]]
# for p0,p1 in data:
#     print(f"{dis(p0,p1)}")

# F
# data = [[(1,), (3,), (7,)], [(1, 1)], [(0, 0), (1, 0),
#                                       (1, 1), (1, 2)], [(0, 0, 0), (1, 1, 1)]]
# for d in data:
#    print(f"{trip(d)}")
