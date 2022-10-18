# Assignment 3

- Username: uzrivera
- Commit hash used for grading: 7b9792fb93baf0432ac3f556b70d04a81b90145e

Grader :Ujjwal Dubey

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 41/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (16/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `N`: 2/2
    - `N_t`: 1/1
    - `W`: 0/1
    - `L`: 1/1
    - TA Comments: TA did not add any comments.

- Problem 2:
    - `q`: 4/5
    - TA Comments: TA did not add any comments.

- Problem 3:
    - `amt`:0/5
    - TA Comments: TA did not add any comments.

- Problem 4:
    - `f`:5/5
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `arithmeticmean`: 1/1
    - `geomean`: 0/2
    - `harmean`: 2/2
    -`rmsmean`: 2/2
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `F`: 0/1 
    - `V`: 0/1
    - `C`: 0/3
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `Mortgage`: 0/2
    - `totalpaid`: 0/3
    - TA Comments: TA did not add any comments.


- Problem 8:
    - `geo`: 0/5
    - `twomin`: 0/1
    - `mm`: 0/2
    - `w`: 0/1
    - `dis`: 0/1
    - `trip`: 0/2
    - TA Comments: TA did not add any comments.

## Code Review & style (25/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to a proper python code.
3. Your logic has to correct.
4. You may pass our test cases but loose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `N`: 2/2
    - `N_t`: 1/1
    - `W`: 0/1
    - `L`: 1/1
    - TA Comments: Please refer to the correct solution for the respective function below:
    def W(P_i, P_f):
    R,T = 8.314, 300
    v = R*T*math.log(P_i/P_f)
    return math.ceil(v)

- Problem 2:
    - `q`: 4/5
    - TA Comments: Please refer to the correct solution for the respective function below:
def q(t):
    a,b,c = t
    discrimant = b**2 - (4*a*c) >= 0
    return discrimant

- Problem 3:
    - `amt`:1.5/5
    - TA Comments: Please refer to the correct solution for the respective function below:
  def m(x,lst):
    is_member = False
    for i in lst:
        if i == x:
            is_member = True
            break
    return is_member

def amt(r,no_tax):
    x,y = 0,0
    for i,j in r:
        if m(i,no_tax):
            y += j
        else:
            x += j
    return round((x*1.07) + y,2)

- Problem 4:
    - `f`: 3/5
    - TA Comments: Please refer to the correct solution for the respective function below:
  def f(p0,p1):
    x0,y0 = p0
    x1,y1 = p1
    if x0 == x1:
        return ()
    else:
        m = (y0-y1)/(x0-x1)
        b = y0 - m*x0
        return m,b


- Problem 5:
    - `arithmeticmean`: 1/1
    - `geomean`: 0.5/2
    - `harmean`: 2/2
    -`rmsmean`: 2/2
    - TA Comments: Please refer to the correct solution for the respective function below:
  def geo_mean(nlst):
    size = len(nlst)
    if 0 in nlst:
        return err_msg[1]
    if nlst:
        base = 10
        sum = 0
        for i in nlst:
            sum += math.log10(i)
        return base**(sum/size)
    else:
        return err_msg[0]


- Problem 6:
    - `F`: 0.5/1 
    - `V`: 0.5/1
    - `C`: 2/3
    - TA Comments: Please refer to the correct solution for the respective function below:
def F(x):
    return 10000

def V(x):
    return -0.0001*(x**2) + 10*x


- Problem 7:
    - `Mortgage`: 1/2
    - `totalpaid`: 1/3
    - TA Comments: Please refer to the correct solution for the respective function below:
def Mortgage(house):
    P, i, t = house
    months = 12
    i, n = (i/100) / months, t*months
    v = (1 + i)**n
    return round(P * ((i*v)/(v-1)),2)

def total_paid(house):
    P, i, t = house
    months = 12
    return round(Mortgage(house)*months*t - P,2)


- Problem 8:
    - `geo`: 1/5
    - `twomin`: 0/1
    - `mm`: 0.5/2
    - `w`: 0.25/1
    - `dis`: 0.25/1
    - `trip`: 0.5/2
    - TA Comments: Please refer to the correct solution for the respective function below:
  def geo(lst,n):
    tmp = []
    a,r = lst[0],lst[1]/lst[0]
    for i in range(n):
        tmp.append(a*(r**i))
    return tmp

def two_min(lst):
    tm_ = lst.copy()
    if len(tm_) > 2:
        a,b,c = tm_[0],tm_[1],tm_[2:]
        for i in c:
            if i < a and a > b:
                a = i
            elif i < b and b > a:
                b = i
    
        tm_ = [a,b]
    a,b = tm_
    if a < b:
        tm_ = [a,b]
    else:
        tm_ = [b,a]
    return tm_

def mm(lst):
    tmp = []
    if lst:
        tmp, rest = [lst[0], 1], lst[1:]
        # print(tmp)
        # print(rest)
        for i in range(len(rest)):
            val = rest[i]
            x,y = tmp
            # print(x, y)
            if val > x:
                tmp = [val, 1]
            elif val == x:
                tmp = [val, y+1]
    return tmp

def mo(lst):
    mtc = True
    if len(lst) > 1:
        s_0,rest = lst[0],lst[1:]
        for s_next in rest:
            if s_next < s_0:
                mtc = False
                break
            else:
                s_0 = s_next
    return mtc

def w(classes, wt):
    tmp = []
    for i in range(len(classes)-1):
        if classes[i] >= wt:
            tmp.append(classes[i])
    return tmp + ["HW"]

def dis(p0,p1):
    result = 0
    for i in range(len(p0)):
        result += (p0[i] - p1[i])**2
    return round(math.sqrt(result),2)

def trip(lst):
    length = 0
    if len(lst) > 1:
        p0,p1,rest = lst[0],lst[1],lst[1:]
        length += dis(p0,p1)
        for r in rest:
            p0,p1 = p1,r 
            length += dis(p0,p1)
    return round(length,2)   
data = [[(1,),(3,),(7,)],[(1,1)],[(0,0),(1,0),(1,1),(1,2)],[(0,0,0),(1,1,1)]]


## Unittest Results
  -------------------------------------
 test_C_3_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 184, in test_C_3_one
     self.assertEqual(a3.C(x),result)
 AssertionError: -5754.456000000006 != 110880.4544
 ======================================
 -------------------------------------
 test_F_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 172, in test_F_1_one
     self.assertEqual(a3.F(rd.randint(100,10000)),10000)
 AssertionError: 10001 != 10000
 ======================================
 -------------------------------------
 test_Mortgage_2_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 203, in test_Mortgage_2_one
     self.assertAlmostEqual(a3.Mortgage(input[i]),result[i],2)
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3.py", line 199, in Mortgage
     c = house[3]
 IndexError: list index out of range
 ======================================
 -------------------------------------
 test_V_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 178, in test_V_1_one
     self.assertAlmostEqual(a3.V(x),result,2)
 AssertionError: -1607079.2010000001 != 247883.07989999998 within 2 places (1854962.2809000001 difference)
 ======================================
 -------------------------------------
 test_W_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 42, in test_W_1_one
     self.assertEqual(a3.W(10,2),4015)
 AssertionError: 2872 != 4015
 ======================================
 -------------------------------------
 test_amt_1_three failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 96, in test_amt_1_three
     self.assertAlmostEqual(a3.amt(r,no_tax),30,2)
 AssertionError: 39 != 30 within 2 places (9 difference)
 ======================================
 -------------------------------------
 test_amt_2_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 76, in test_amt_2_one
     self.assertAlmostEqual(a3.amt([[2, 2.00], [3, 10.00], [4, 1.5], [1, 5.0]], [4, 1, 5]),19.34,2)
 AssertionError: 29.5 != 19.34 within 2 places (10.16 difference)
 ======================================
 -------------------------------------
 test_amt_2_two failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 80, in test_amt_2_two
     self.assertAlmostEqual(a3.amt([[1, 3.0], [2, 1.25], [3, 100], [10, 0.75]], [10, 3, 22, 41, 85]),105.3,2)
 AssertionError: 129.0 != 105.3 within 2 places (23.700000000000003 difference)
 ======================================
 -------------------------------------
 test_dis_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 281, in test_dis_1_one
     self.assertAlmostEqual(a3.dis(lst1,lst2),result,2)
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3.py", line 317, in dis
     total += (lst_total)
 TypeError: unsupported operand type(s) for +=: 'int' and 'list'
 ======================================
 -------------------------------------
 test_f_3_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 114, in test_f_3_one
     self.assertEqual(a3.f((x0,y0),(x1,y1)),(m,b))
 AssertionError: Tuples differ: (-0.08333333333333333, 2.333333333333333) != (-0.08333333333333333, 2.3333333333333335)
 
 First differing element 1:
 2.333333333333333
 2.3333333333333335
 
 - (-0.08333333333333333, 2.333333333333333)
 + (-0.08333333333333333, 2.3333333333333335)
 ?                                         +
 
 ======================================
 -------------------------------------
 test_geo_2_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 240, in test_geo_2_one
     self.assertEqual(a3.geo(input[i][0],input[i][1]),output[i])
 AssertionError: Lists differ: [1, -3, 9.0] != [1.0, -3.0, 9.0, -27.0]
 
 Second list contains 1 additional elements.
 First extra element 3:
 -27.0
 
 - [1, -3, 9.0]
 + [1.0, -3.0, 9.0, -27.0]
 ======================================
 -------------------------------------
 test_geo_3_two failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 249, in test_geo_3_two
     self.assertEqual(a3.geo(i,j),result)
 AssertionError: Lists differ: [-8, 6, -4.5] != [-8.0, 6.0, -4.5, 3.375, -2.53125, 1.8984375[62 chars]4375]
 
 Second list contains 7 additional elements.
 First extra element 3:
 3.375
 
 - [-8, 6, -4.5]
 + [-8.0,
 +  6.0,
 +  -4.5,
 +  3.375,
 +  -2.53125,
 +  1.8984375,
 +  -1.423828125,
 +  1.06787109375,
 +  -0.8009033203125,
 +  0.600677490234375]
 ======================================
 -------------------------------------
 test_geomean_2_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 145, in test_geomean_2_one
     self.assertAlmostEqual(a3.geo_mean(lst),result,2)
 AssertionError: 12 != 34.11437325862954 within 2 places (22.11437325862954 difference)
 ======================================
 -------------------------------------
 test_mm_2_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 261, in test_mm_2_one
     self.assertEqual(a3.mm(lst),a3_sol.mm(lst))
 AssertionError: Lists differ: [10, 1] != [10, 3]
 
 First differing element 1:
 1
 3
 
 - [10, 1]
 ?      ^
 
 + [10, 3]
 ?      ^
 
 ======================================
 -------------------------------------
 test_mo_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 266, in test_mo_1_one
     self.assertEqual(a3.mo(lst),a3_sol.mo(lst))
 AssertionError: True != False
 ======================================
 -------------------------------------
 test_q_1_three failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 72, in test_q_1_three
     self.assertEqual(a3.q([4, 4, 1]),True)
 AssertionError: False != True
 ======================================
 -------------------------------------
 test_totalpaid_3_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 221, in test_totalpaid_3_one
     self.assertAlmostEqual(a3.total_paid(input[i]),result[i],2)
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3.py", line 213, in total_paid
     c = house[3]
 IndexError: list index out of range
 ======================================
 -------------------------------------
 test_trip_2_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 299, in test_trip_2_one
     self.assertAlmostEqual(a3.trip(input[i]),output[i],2)
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3.py", line 333, in trip
     total += dis(lst[i-1], lst[i])
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3.py", line 317, in dis
     total += (lst_total)
 TypeError: unsupported operand type(s) for +=: 'int' and 'list'
 ======================================
 -------------------------------------
 test_twomin_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 255, in test_twomin_1_one
     self.assertEqual(a3.two_min(lst),a3_sol.two_min(lst))
 AssertionError: (12, 13) != [12, 13]
 ======================================
 -------------------------------------
 test_w_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3_hidden_tests.py", line 273, in test_w_1_one
     self.assertEqual(a3.w(lst,weight),a3_sol.w(lst,weight))
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\uzrivera\a3.py", line 292, in w
     classes[9] = 200
 IndexError: list assignment index out of range
 ======================================
