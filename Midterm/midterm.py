########
########
# Write you code for midterm problems in this file.
# Do not change the name of this file.
########

# Your functions goes here
import math
# Problem 1


def f(xlst, n):
    nlst = []
    for i in xlst:
        if len(i) > n:
            nlst.append(i)
    return nlst

# Problem 2


def gravity(m1, m2, d):
    G = 6.67*10**-11
    return G*m1*m2/d**2


if __name__ == "__main__":

    """
If you want to do some of your own testing in this file, 
please put any print statements you want to try in 
this if statement.

Please comment the print statements before submitting your 
final version.
    """


# Problem 1


# xlst = [[1, 2, 3], [1, 2], [1, 2, 3, 4], [1]]
# print(f(xlst, 0))
# print(f(xlst, 1))
# print(f(xlst, 3))

# Problem 2

# m1, m2, d = 1, 6*math.exp(24), 4*math.exp(6)
# print(gravity(m1, m2, d))

# Finished
