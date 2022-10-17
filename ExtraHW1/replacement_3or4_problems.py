import math

# leave unchanged if working individually
# My Partner is ________________________


# problem 1
# input 0,1,2,...
# return factorial
def factorial(n):
    a = math.factorial(n)
    return a

# problem 2
# input two lists (containing numbers) of same length
# return a list of the greater number at each position of the input lists


def gl(lst1, lst2):
    z = 0
    y = 0
    nlst = []
    for i in range(len(lst1)):
        if lst1[i] >= lst2[i]:
            z = lst1[i]
            nlst.append(z)
        elif lst1[i] <= lst2[i]:
            y = lst2[i]
            nlst.append(y)
    return nlst

    # problem 3
    # INPUT argument n and number of terms
    # RETURN approximation of e(n) for num_terms.


def my_e(n, num_terms):
    e = 0
    for i in range(num_terms+1):
        e += n**i/factorial(i)
    return e

    # problem 4
    # INPUT a string
    # RETURN a dictionary of all the proper substrings with counts of occurences


def ss(x):
    pass


# problem 5
# INPUT old, new, list of lists
# RETURN for each list in list, replace old with new
def lst_replace(old, new, lst):
    nlst = []
    for num_lst in lst:
        for i in num_lst:
            if i == old:
                nlst.append(new)
            else:
                nlst.append(i)
    return nlst

    pass


# problem 6
# INPUT list
# INPUT remove any list brackets objects are in the same order
def foo(lst):
    pass


if __name__ == "__main__":

    """uncomment if you'd like"""

    # # problem 1
    for i in range(6):
        print(f"{i}! = {factorial(i)}")

    # # # # problem 2
    p2 = [[[1, 0, 0, 1], [0, 1, 1, 0]], [[], []], [[1, 2, 3, 4], [5, 4, 3, 2]]]

    for x, y in p2:
        print(f"{x,y} {gl(x,y)}")

    # problem 3
    print(math.exp(5))
    print(my_e(5, 16))

    # #problem 4
    # p4 = ["s","abc","abcabc","aa"]
    # for d in p4:
    #     print(d)
    #     print(ss(d))

    # problem 5
    # lst = [[1, 2], [2, [2], 1], [], [1, 1, ]]
    # print(lst_replace(1, "dog", [[1, 2], [2, [2], 1], [], [1, 1, ]]))
    # print(lst_replace(2, "dog", [[1, 2], [2, [2], 1], [], [1, 1, ]]))
    # print(lst_replace([2], "dog", [[1, 2], [2, [2], 1], [], [1, 1, ]]))
    # print(lst_replace(1, "dog", []))

    # #problem 6
    # p6 = [[[1],2,[[3]]], [[1,[2,[3]],4,[[5]],6,[7,8]]],
    #     [1,2,3,[[[4]]]],[],[1,2,3]]

    # for d in p6:
    #     print(f"{d} \n {foo(d)}")
