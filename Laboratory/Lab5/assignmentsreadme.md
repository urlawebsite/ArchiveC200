#### Code1

```python
#problem 5
#input [arg1,op,arg2,ans]
#output arg1 op arg2 == ans

def eq(lst):
    for item in lst:
     if item[0] * item[2] >= item[3]:
        return True
    else:
        return False
```

-------------------------------------

#### Unittest Results1

test_eq_2_four failed.

Traceback (most recent call last):
  File "a2_hidden_test.py", line 164, in test_eq_2_four
    self.assertEqual(a2.eq([arg1, op[0], arg2, result]), True)
  File "D:\IndianaUniversity\Semester2\AI_C200_Spring2022\Spring-2022\Labs\Lab5-\a2.py", line 68, in eq
    if item[0] * item[2] >= item[3]:
TypeError: 'int' object is not subscriptable

-------------------------------------

#### Explanation1:

test_eq_2_four failed: This here means that function name that we used to test the code for eq function. 

Here it’s eq_2 -that’s a naming we use for different tests.  So, different tests can have different 
names like eq_1_two, eq_1_three – students don’t have to really be concerned about these names 
unless you think there is a case that incorrectly graded you then you can explicitly point to it by 
name when you talk to us.

Line1 a2_hidden_test.py:  It is the name of our test file that contains all the cases for all the problems. It’s similar to unit test file that we put in your repo.

self.assertEqual(a2.eq([arg1, op[0], arg2, result]), True): a2 here is your assignment2 python file. So, in this example, we ran function eq in your a2.  

 a2.eq([arg1, op[0], arg2, result]), True) – the expected output is True

TypeError: 'int' object is not subscriptable: This is the exact error why the test failed. In this case, item is an integer so it does not make sense to write "if item[0] * item[2] >= item[3]:"

-------------------------------------

#### Code2
```python
#problem 2
#input year 1977-1997
#return percent income or "error: year" if year 
#is outside range
lst = [1977,1997]
def f(t):
    for i in range(0,len(lst)):
        if 1977 < i <= 1984:
            return 2/7 * (t - 1977) + 12
        elif 1984 < t <= 1977:
            return (t - 1977) + 7
        elif 1987 < t < 1997:
             return 3/5 * (t - 1977) + 11
        else:
            return "error:year"
```
-------------------------------------
#### Unittest Results2

test_f_1_three failed.

Traceback (most recent call last):
  File "a2_hidden_test.py", line 55, in test_f_1_three
    self.assertEqual(a2.f(1976), error_string)
AssertionError: 'error:year' != 'error: year'
- error:year
+ error: year
?       +


-------------------------------------

#### explanation2:

test_f_1_three failed: This here means that function name that we used to test the code for function f. 


self.assertEqual(a2.f(1976), error_string): a2 here is your assignment2 python file. So, in this example, we ran function f in your a2.  

 self.assertEqual(a2.f(1976), error_string) – the expected output is error_string (if you look into the s2_hidden_test.py file you'll see the error _string variable is equal to 'error: year')

TypeError: AssertionError: 'error:year' != 'error: year'
- error:year
+ error: year"

As you see these two strings are not equal so the unit test raised an error.


--------------------------------------
#### Code3
```python
#problem 1
#input real
#return real
def g(x):
    if x != 0:
        return x + 2
    else:
        return 1
```
-------------------------------------
#### Unittest result3:

test_g_4_one failed.

Traceback (most recent call last):
  File "a2_hidden_test.py", line 16, in test_g_4_one
    self.assertAlmostEqual(a2.g(0), 2, 2)
AssertionError: 1 != 2 within 2 places (1 difference)

-------------------------------------

#### Explanation3:

test_g_4_one failed.: This here means that function name that we used to test the code for function g. 


self.assertAlmostEqual(a2.g(0), 2, 2): a2 here is your assignment2 python file. So, in this example, we ran function g in your a2.  

self.assertAlmostEqual(a2.g(0), 2, 2) – the expected output is 2 (with approximately equal up-to 2 decimal places) 

TypeError: AssertionError: 1 != 2 within 2 places (1 difference)

As you see the output if the funtion is 1 but the expected output is 2 and these two are not equal


-------------------------------------
#### Code4:
```python
#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x,y,z):
    print(max2d(x, max2d(y,z)))
```

-------------------------------------
#### Unittest results4:

test_max3d_1_five failed.

Traceback (most recent call last):
  File "a2_hidden_test.py", line 234, in test_max3d_1_five
    self.assertEqual(a2.max3d(1,2,3), 3)
AssertionError: None != 0


-------------------------------------
#### Explanation4:

test_max3d_1_five failed: This here means that function name that we used to test the code for max3d function. 


self.assertEqual(a2.max3d(1,2,3), 0): a2 here is your assignment2 python file. So, in this example, we ran function g in your a2.  

self.assertEqual(a2.max3d(1,2,3), 3) – the expected output is 3 

TypeError: AssertionError: None != 3
In the function there is a print statement and not the return, so the function will return None by default but the expected output is 3.





