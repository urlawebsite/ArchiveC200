import math
from re import A, I

# Problem 1
# INPUT list of 0 and 1
# RETURN the COUNT of the longest sequence of concecutive 1s is returned


def ls(x):
    for i in x:

        # for num in len(x):

        #   for num in x:
        #       if num == 1 and num != 0:
        #           totalc += 1

        ###########################################################################
        # Problem 2
        ###########################################################################

        # INPUT two lists of 0s and 1s. Think of each list as representing a person
        # as explained in the HW PDF.
        # RETURN inner product.


def inner_prod(v0, v1):
    x = v0
    y = v1
    new = 0
    total = 0
    for i in x:
        print(i)
        print(y)

    return total

# INPUT a list of 0s, 1s
# RETURN square root of inner product


def mag(v):
    pass

# INPUT two lists of 0s, 1s
# RETURN angle in degrees


def angle(v0, v1):
    pass

# INPUT list of people
# RETURN unique pairs with angle


def match(people):
    pass

# INPUT list of pairs with angle
# RETURN best pair (smallest angle)


def best_match(scores):
    pass

###########################################################################
# Problem 3
###########################################################################
# INPUT two lists like [m ,b]. Each list represents a line in slop, intercept form.
# RETURN 2D point of intersection in the format [x-coordinate, y-coordinate].


def intersect(d0, d1):
    pass

###########################################################################
# Problem 4
###########################################################################
# INPUT list of numbers
# RETURN dictionary of relative frequency of members in the list


def make_prob(xlst):
    pass

###########################################################################
# Problem 5
###########################################################################
# INPUT list of numbers
# RETURN entropy of probability function


def entropy(lst):
    pass


###########################################################################
# Problem 6
###########################################################################
# INPUT List of numbers
# RETURN mean
def mean(lst):
    pass

# INPUT list of numbers
# RETURN variance


def variance(lst):
    pass


# INPUT list of numbers
# RETURN standard deviation (sqrt of variance)
def std(lst):
    pass


# INPUT list of numbers
# RETURN list of mean centered numbers
def mean_centered(lst):
    pass


###########################################################################
# Problem 7
###########################################################################
# INPUT list of numbers and option 0, 1
# RETURN absolutest greatest difference if option = 1, and smallest if option = 0
def blist(lst):
    pass


###########################################################################
# Problem 8
###########################################################################
# INPUT lists of data logs [name,[s1,t1],[s2,t2],...]
# RETURN the name and most mileage
def f_(xlst):
    pass


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file,
    please put any print statements you want to try in
    this if statement.

    If you uncomment the following print statements for testing
    then please comment them back before submitting your final version.

    You are encouraged to do some of your own testing by
    trying different values as function parameters in the print
    statements.
    """

    # #problem 1
    p1 = [[0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [0, 0], [1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 0, 0]]
    for x in p1:
        print(f"{x}  {ls(x)}")

    # #problem 2
    #people0 = [[0, 1, 1], [1, 0, 0], [1, 1, 1]]
    # print(match(people0))
    # print(best_match(match(people0)))

    # people1 = [[0,1,1,0,0,0,1],
    #            [1,1,0,1,1,1,0],
    #            [1,0,1,1,0,1,1],
    #            [1,0,0,1,1,0,0],
    #            [1,1,1,0,0,1,0]]
    # print(best_match(match(people1)))

    #v0, v1 = (2, 3, -1), (1, -3, 5)
    # print(f"122 deg = {angle(v0,v1)}") #122

    #v0, v1 = (2, 3, -1), (1, -3, 5)
    #print(inner_prod(v0, v1))
    # v0,v1 = (3,4,-1),(2,-1,1)
    # print(f"85.41 deg = {angle(v0,v1)}") #85.41

    # v0,v1 = (5,-1,1),(1,1,-1)
    # print(f"70.53 deg = {angle(v0,v1)}") #70.53

    # #problem 3
    # l0 = (2,3)
    # l1 = (-1/2,2)
    # print(intersect(l0,l1)) #-2/5,11/5
    # print(intersect((1,4),(-1/2,1/2)))

    # #problem 4
    # p4 = [[1,1,0,0],[1,2,3,1,1,2,1],['a','a','b']]

    # for d in p4:
    #     print(f"{d} {make_prob(d)}")

    # #problem 5
    # p5 = [[1,1,0,0],[1,2,3,1,1,2,1],['a','a','b']]
    # for d in p5:
    #     print(f"{entropy(d)}")

    # #problem 6
    # p6 = [1,3,3,2,9,10]
    # print(f"mean {mean(p6)}")
    # print(f"variance {variance(p6)}")
    # print(f"std {std(p6)}")
    # print(f"mean centered {mean(mean_centered(p6))}")

    # # problem 7
    # p7 = [[[6,2,1,100],1],[[6,2,1,100],0],[[0,0,10,10],1],
    #    [[1,2,1,-4],0],[[1,2,1,-4],1],[[0,0,10,10],0]]
    # for d in p7:
    #     print(f"{d} {blist(d)}")

    # #problem 8
    # truck_d = [['X', [ 55,[0,60]],[15,[2.5]],[75,[.2,48]]],
    #        ['Y', [55,[0,60]]],
    #        ['Z', [10,[1]],[10,[1]]],
    #        ['A', [30,[2]]]]
    # print(f"{f_(truck_d)}")
