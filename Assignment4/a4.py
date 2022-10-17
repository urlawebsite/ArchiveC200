import math


# Problem 1
# INPUT list of 0 and 1
# RETURN the COUNT of the longest sequence of concecutive 1s is returned


def ls(x):
    a = 0
    b = 0
    for num in x:
        if num == 1:
            b += 1
        else:
            a = max(a, b)
            b = 0
    return max(a, b)

    ###########################################################################
    # Problem 2
    ###########################################################################

    # INPUT two lists of 0s and 1s. Think of each list as representing a person
    # as explained in the HW PDF.
    # RETURN inner product.


def inner_prod(v0, v1):
    disdict = []
    total = 0
    for i in range(len(v0)):
        disdict.append(v0[i]*v1[i])
    for num in disdict:
        total += num
    return total

# INPUT a list of 0s, 1s
# RETURN square root of inner product


def mag(v):
    total = math.sqrt(inner_prod(v, v))
    return total

# INPUT two lists of 0s, 1s
# RETURN angle in degrees


def angle(v0, v1):
    delta = (180/math.pi)*math.acos(inner_prod(v0, v1) /
                                    round(mag(v0)*mag(v1), 99))
    return round(delta, 2)

# INPUT list of people
# RETURN unique pairs with angle


def match(people):
    disdict = []
    total = 0
    for i in range(0, len(people)):
        for j in range(i+1, len(people)):
            total = angle(people[i], people[j])
            disdict.append([people[i], people[j], total])
    return disdict

# INPUT list of pairs with angle
# RETURN best pair (smallest angle)


def best_match(scores):
    best = scores[0]
    for i in range(len(scores)):
        if scores[i]:
            if scores[i][2] < best[2]:
                best = scores[i]
    return best
###########################################################################
# Problem 3
###########################################################################
# INPUT two lists like [m ,b]. Each list represents a line in slop, intercept form.
# RETURN 2D point of intersection in the format [x-coordinate, y-coordinate].


def intersect(d0, d1):
    y1 = d1[1]
    x1 = d1[0]
    y0 = d0[1]
    x0 = d0[0]
    p1 = y1 - y0
    p2 = x0 - x1
    p3 = p1 * (p2)**-1
    p4 = x1*(p3) + y1
    y = round(p4, 2)
    x = round(p3, 2)
    return x, y

    ############################
    # ##############################################
    # Problem 4
    ###########################################################################
    # INPUT list of numbers
    # RETURN dictionary of relative frequency of members in the list


def make_prob(xlst):
    count = {}
    n = len(xlst)
    for num in xlst:
        if num in count.keys():
            count[num] += round(1 * 1/n, 2)
        else:
            count[num] = round(1 * 1/n, 2)
    return count


###########################################################################
# Problem 5
###########################################################################
# INPUT list of numbers
# RETURN entropy of probability function


def entropy(lst):
    x = []
    ent = make_prob(lst)
    ent2 = ent.values()
    for i in ent2:
        x.append(i*math.log2(1/i))
    sum = 0
    for _ in x:
        sum += _
    return round(sum, 2)
    pass


###########################################################################
# Problem 6
###########################################################################
# INPUT List of numbers
# RETURN mean
def mean(lst):
    n = len(lst)
    total = 0
    m = 0
    for i in lst:
        total += i
        m = total/n

    return round(m, 2)

# INPUT list of numbers
# RETURN variance


def variance(lst):
    n = 1/len(lst)
    i = mean(lst)
    t = []
    p = []
    tp = 0
    for num in lst:
        t.append(num - i)
    for numt in t:
        p.append(numt**2)
    for nump in p:
        tp += nump * n
    return round(tp, 2)

    # INPUT list of numbers
    # RETURN standard deviation (sqrt of variance)


def std(lst):
    value = math.sqrt(variance(lst))
    return round(value, 2)

# INPUT list of numbers
# RETURN list of mean centered numbers


def mean_centered(lst):
    u = mean(lst)
    disdict = []
    for num in lst:
        disdict.append(num - u)
    return disdict
    pass


###########################################################################
# Problem 7
###########################################################################
# INPUT list of numbers and option 0, 1
# RETURN absolutest greatest difference if option = 1, and smallest if option = 0
def blist(lst):
    for i in range(len(lst)):
        if lst[1] == 1:
            return max(lst[0])-(min(lst[0]))
        else:
            small = [abs(j) for j in lst[0]]
            small.sort()
            smallest = small[0] - small[1]
            return abs(smallest)

    ###########################################################################
    # Problem 8
    ###########################################################################
    # INPUT lists of data logs [name,[s1,t1],[s2,t2],...]
    # RETURN the name and most mileage


def f_(xlst):
    disdict = {}
    for i in xlst:
        fdis = 0
        for j in i[1:]:
            if len(j[1]) == 2:
                dis = j[0]*(j[1][0] + (j[1][1] * 1/60))
            else:
                dis = j[0]*j[1][0]
            fdis += dis
        disdict[i[0]] = fdis
    disdict = {k: v for k, v in sorted(dict.items(
        disdict), key=lambda item: [1], reverse=True)}
    result = list(list(disdict.items())[0])
    return result


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

    # problem 1
    p1 = [[0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [0, 0], [1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 0, 0]]
    for x in p1:
        print(f"{x}  {ls(x)}")

    # problem 2
    people0 = [[0, 1, 1], [1, 0, 0], [1, 1, 1]]
    print(match(people0))
    print(best_match(match(people0)))

    people1 = [[0, 1, 1, 0, 0, 0, 1],
               [1, 1, 0, 1, 1, 1, 0],
               [1, 0, 1, 1, 0, 1, 1],
               [1, 0, 0, 1, 1, 0, 0],
               [1, 1, 1, 0, 0, 1, 0]]
    print(best_match(match(people1)))

    v0, v1 = (2, 3, -1), (1, -3, 5)
    print(f"122 deg = {angle(v0,v1)}")  # 122

    v0, v1 = (2, 3, -1), (1, -3, 5)
    print(inner_prod(v0, v1))
    v0, v1 = (3, 4, -1), (2, -1, 1)
    print(f"85.41 deg = {angle(v0,v1)}")  # 85.41

    v0, v1 = (5, -1, 1), (1, 1, -1)
    print(f"70.53 deg = {angle(v0,v1)}")  # 70.53

    # problem 3
    l0 = (2, 3)
    l1 = (-1/2, 2)
    print(intersect(l0, l1))  # -2/5,11/5
    print(intersect((1, 4), (-1/2, 1/2)))

    # problem 4
    p4 = [[1, 1, 0, 0], [1, 2, 3, 1, 1, 2, 1], ['a', 'a', 'b']]

    for d in p4:
        print(f"{d} {make_prob(d)}")

    # problem 5
    p5 = [[1, 1, 0, 0], [1, 2, 3, 1, 1, 2, 1], ['a', 'a', 'b']]
    for d in p5:
        print(f"{entropy(d)}")

    # problem 6
    p6 = [1, 3, 3, 2, 9, 10]
    print(f"mean {mean(p6)}")
    print(f"variance {variance(p6)}")
    print(f"std {std(p6)}")
    print(f"mean centered {mean(mean_centered(p6))}")

    # problem 7
    p7 = [[[6, 2, 1, 100], 1], [[6, 2, 1, 100], 0], [[0, 0, 10, 10], 1],
          [[1, 2, 1, -4], 0], [[1, 2, 1, -4], 1], [[0, 0, 10, 10], 0]]
    for d in p7:
        print(f"{d} {blist(d)}")

    # problem 8
    truck_d = [['X', [55, [0, 60]], [15, [2.5]], [75, [.2, 48]]],
               ['Y', [55, [0, 60]]],
               ['Z', [10, [1]], [10, [1]]],
               ['A', [30, [2]]]]
    print(f"{f_(truck_d)}")

# My Tests

# x0 = [1, 0, 0]
# x1 = [1, 1, 1]
# print(inner_prod(x1, x0))
# print(mag(x0))
# print(mag(x1))
# print(angle(x0, x1))


# people0 = [[0, 1, 1], [1, 0, 0], [1, 1, 1]]
# print(match(people0))
# print(best_match(match(people0)))
