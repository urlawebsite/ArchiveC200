# Write the name of your programming partner below
# partner name: Anthony Reyes

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib
# import os

###############
# PROBLEM ONE
###############

# choice
# You can choose this function to complete B()


def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return C(n-1, k) + C(n-1, k-1)

# Input: a number n
# Return: The output of B as per HW instructions


def B(n):
    if n == 0:
        return 1
    else:
        k = 0
        nlst = []
        while k <= n-1:
            nlst += [C(n+1, k)*B(k)]
            k = k+1
        return (sum(nlst)*-1)/(n+1)

        ###############
        # PROBLEM TWO
        ###############

        # Input: a number n
        # Return: The output of a() as per HW instructions


def a(n):
    if n == 1:
        return 3
    if n == 2:
        return 5
    if n == 0:
        return 2
    else:
        return a(n-1)+a(n-2)+a(n-3)

# Input: a number n
# Return: The output using while loop


def aw(n):
    b = 0
    nlst = []
    while b != n+1:
        b = b + 1
        nlst.append(a(b-1))
    return nlst[n]

# Input: generator don't need to have any input. Instead, you can set the base case values and then
# use 'yield' keyword inside a loop
# Return: The output via using generators


def a_gen():
    for i in range(0, 10):
        yield aw(i)

# Input: a number n
# Return: The output using tail recursion


def at(n, v0=2, v1=3, v2=5):
    if n == 0:
        return v0
    if n == 1:
        return v1
    if n == 2:
        return v2
    else:
        return at(n-1)+at(n-2)+at(n-3)

# Input: a number x
# Return: The output of bb() as per HW instructions


def bb(x):
    if x == 0:
        return 2
    if x == 1:
        return -3
    else:
        return bb(x-1)*bb(x-2)

# Input: a number x
# Return: The output using while loop


def bbw(x):
    b = 0
    t = [2]
    while b != x:
        b += 1
        t.append(bb(b))
    return t[-1]

# Input: generator don't need to have any input. Instead, you can set the base case values and then
# use 'yield' keyword inside a loop
# Return: The output via using generators


def bb_gen():
    for i in range(0, 10):
        yield bb(i)

# Input: a number n
# Return: The output using tail recursion


def bbt(x, v0=2, v1=-3):
    if x == 0:
        return v0
    if x == 1:
        return v1
    else:
        return bbt(x-1)*bbt(x-2)

# Input: numbers n, m ,p
# Return: The output of F() as per HW instructions


def F(n, m, p):
    if p == 0:
        return 100+n-m
    else:
        return m*n-p+F(n-3, m-2, p-1)

# Input: a number n, m ,p
# Return: The output using tail recursion


def Ft(n, m, p, v=100):
    if p == 0:
        t = 100 + n-m
        return t
    else:
        x = 100 + n-m
        t = Ft(n-3, m-2, p-1, x-1)
        return t-p+(m*n)

# Input: a number n, m, p
# Return: The output using while loop


def Fw(n, m, p):
    b = p
    if p == 0:
        return 100+n-m
    else:
        while b != 0:
            x = Fw(n-3, m-2, p-1)
            b -= 1
    return x-p+(m*n)


def m(x, y):
    if x <= 0 and y <= 0:
        return 3
    elif x <= 0:
        return 2
    elif y <= 0:
        return 1
    else:
        return m(x-1, y-1) + m(x-1, y-2)

# Input: numbers x and y
# Return: The output using while loop


def mw(x, y):
    while True:
        if x <= 0 and y <= 0:
            return 3
        elif x <= 0:
            return 2
        elif y <= 0:
            return 1
        else:
            return m(x-1, y-1) + m(x-1, y-2)


###############
# PROBLEM THREE
###############

# INPUT takes path + filename (I am using a txt file)
# RETURN returns list of tuples [(year,population),...], stick to the format of return values.
def get_data(path, name):
    title = "Years + 1900    Population x10^6"
    with open(name, "w") as path:
        path.write(title + '\n')
    data = [(0, 1650), (10, 1750), (20, 1860), (30, 2070), (40, 2300), (50, 2560),
            (60, 3040), (70, 3710), (80, 4450), (90, 5280), (100, 6080), (110, 6870)]
    for items in data:
        with open(name, "a") as path:
            path.write(str(items[0]) + " " + str(items[1]) + '\n')
    return data

# Input: a year
# Return: the estimate of population for that year


def pop(year):
    return 1436.53*(1.01395**year)


# Input: data
# Return: the average error as per equation 18.

def error(data):
    a = 0
    for i in range(0, 12):
        a += ((data[i][1])-pop(i*10))
    return (1/(len(data)))*a

###############
# PROBLEM four
###############
# You cannot simply divide or use modulus
# You must implement the algorithm as described
# INPUT a number n
# RETURN True if dvisible by 11, False if not.


def div_11(n):
    lst = [i for i in str(n)]
    sumEven = 0
    sumOdd = 0
    for even in lst[::2]:
        sumEven += int(even)
    for odd in lst[1::2]:
        sumOdd += int(odd)
    if sumOdd-sumEven == 0:
        return True
    elif sumOdd-sumEven == 11:
        return True
    elif sumOdd-sumEven == -11:
        return True
    else:
        return False


###############
# PROBLEM five
###############
# INPUT list of numbers
# RETURN list of nesting level and sum at that level
def sl(lst, p=0):
    nlst = []
    sum = 0
    nlst1 = []
    nlst2 = []
    if len(lst) == 0:
        return nlst2
    for num in lst:
        if type(num) == list:
            continue
        else:
            nlst += [num]
    for num in nlst:
        lst.remove(num)
        sum += num
    for num in lst[0:]:
        nlst1 += num
    lst = nlst1
    nlst2 += [[p, sum]]
    return nlst2 + sl(lst, p+1)

    #         nlst.append(nums)
    #     elif nums == list:
    #         n1lst.append(nums)
    # return nlst
    # PROBLEM 6
    # Uncomment the following code after finishing the population problem
    # Please remember to comment it back before submitting to the Autograder
    # We will mnaually run the code to see if the code correctly draws the trainagles.
    # import pygame, sys
    # import math
    # from pygame.locals import *
    # import random as rn
    # pygame.init()

    # BLUE = (0,0,255)
    # WHITE = (255,255,255)
    # BLACK = (0,0,0)

    # DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)

    # pygame.display.set_caption('S-Triangle')

    # INPUT takes a location loc = (x,y) pair of points and width
    # RETURN 3 points of the equilateral triangle determined by loc and width
    # def triangle(loc,width):
    #     x,y = loc
    #     z = math.sqrt(width**2 - (width/2))
    #     return (x,y),(x - width/2,y + z),(x + width/2, y + z)

    # DISPLAYSURF.fill(BLACK)

    # Draws Triangle
    # (triangle(loc,w)) is a tuple of tuples...)
    # def draw_triangle(loc, w):
    #     pygame.draw.polygon(DISPLAYSURF, (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255)) , (triangle(loc,w)),1)

    # INPUT location and width
    # RETURN nothing -- follows algorithm
    # Draw the three smaller triangles as described
    # in the text
    # def s(loc,width):
    #     if width > 1:
    #         x,y = loc
    #         z = math.sqrt(width**2 - (width/2))
    #         draw_triangle(loc,width)
    #     else:
    #         return


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test
    your code outside of the `test_a7.py`. Feel free to add print statements.
    # """

    # PROBLEM 1

    # for i in range(6):
    #     print("B({0}) = {1}".format(i, B(i)))

    # PROBLEM 2
    # for i, j in zip(range(10), a_gen()):
    #     print(f"a({i}) {a(i)} {aw(i)} {at(i)} {j} \n", end="")
    # for i, j in zip(range(10), bb_gen()):
    #     print(f"b({i}) {bb(i)} {bbw(i)} {bbt(i)} {j}")
    # for i in range(6):
    #     for j in range(6):
    #         for k in range(6):
    #             print(f"{i,j,k} {F(i,j,k)} {Ft(i,j,k)} {Fw(i,j,k)}")
    # for i in range(10):
    #     for j in range(10):
    #         print(f"{i,j} {m(i,j)} {mw(i,j)} ")

    # Problem 3
    # data = get_data(".", "pop.txt")
    # print(f"data from file:", data)
    # print(f"abs(3040 - {pop(60)}) = {abs(3040 - pop(60))}")
    # ave_error = round(error(data), 2)
    # print(f"Average error: {ave_error}")

    # #uncomment to see plot
    # Please comment it back after you are done
    # completing the functions, otherwise the Autograder will
    # return with error.

    # t = np.arange(0.0, 120.0)
    # fig, ax = plt.subplots()

    # ax.plot(t, pop(t), 'g')
    # for y, p in data:
    #     ax.plot(y, p, 'ro--')

    # ax.set(xlabel="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    #        title="Population Model Average Error = {0}".format(ave_error))
    # ax.grid()
    # plt.show()

    # problem 4
    # nlst = [587657752,11,22,2728,31415,1358016]
    # for n in nlst:
    #     print(div_11(n), n / 11)

    # # problem 5
    # prob5 = [[1, 4, [3, [100]], 3, 2, [1, [101, 1000], 5], 1, [7, 9]],
    #          [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400]]],
    #          [[[[100, 200, 300, 400]]], [[10, 20, 30, 40]], 1, 2, 3, 4]]
    # for lst in prob5:
    #     print(sl(lst))

    # Problem 6
    # s((240,0),440)

    # while True:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             pygame.quit()
    #             sys.exit()
    #     pygame.display.update()
