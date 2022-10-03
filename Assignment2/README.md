# Assignment 2

- Username: uzrivera
- Commit hash used for grading: 011047af0fce3dabd77f26a4b424bbf525a4e271

Rubric (see Canvas page):Srinivas Vaddi

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score:85/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (37.0/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `g`: 5.0/5
    - TA Comments: TA did not add any comments.

- Problem 2:
    - `f`: 5.0/5
    - TA Comments: TA did not add any comments.

- Problem 3:
    - `h_0`: 1.0/1
    - `h_1`: 1.0/1
    - `h`: 3.0/3
    - TA Comments: TA did not add any comments.

- Problem 4:
    - `q`: 0.0/5
    - TA Comments: In this function, although you are calculating the discriminant, there is no validatio for the discriminant. The equation implementation is incorrect. It should be ` (b + math.sqrt((b**2) - (4*a*c))) / (2*a)`


- Problem 5:
    - `eq`: 5.0/5
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `path`: 3.0/5
    - TA Comments: `else` cases are missing the `if` conditions that are required. Please look at the failing testcases for more information. As an example, you are checking `if lst[0] == 1:` however the else case here is not handled. The reason as to why it is important is that, if s0 is open the electricity doesnt flow. So it must return False. However that case is missing.


- Problem 7:
    - `max2d`: 3.0/3
    - `max3d`: 5.0/5
    - TA Comments: Overriding unit-test score

- Problem 8:
    - `Rectangle`: 5.0/5
    - `box`: 2.0/2
    - `rR`: 0.0/5
    - TA Comments: Rounding should be in place for both the fuction `rR`. That is only till 2 decimal places and not to next number

## Code Review & style (48/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to a proper python code.
3. Your logic has to correct.
4. You may pass our test cases but loose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

  Problem 1:
    - `g`: 5/5
    - TA Comments: TA did not add any comments.

- Problem 2:
    - `f`: 5/5
    - TA Comments: TA did not add any comments.

- Problem 3:
    - `h_0`: 1/1
    - `h_1`: 1/1
    - `h`: 3/3
    - TA Comments: TA did not add any comments.

- Problem 4:
    - `q`: 3/5
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `eq`: 5/5
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `path`: 5/5
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `max2d`: 3/3
    - `max3d`: 5/5
    - TA Comments: TA did not add any comments.

- Problem 8:
    - `Rectangle`: 5/5
    - `box`: 2/2
    - `rR`: 5/5
    - TA Comments: TA did not add any comments.



## Unittest Results
-------------------------------------

test_max3d_1_five failed.



Traceback (most recent call last):

  File "C:\Users\smish\Spring-2022\Gradingdata\Assignment2\uzrivera\a2_hidden_test.py", line 205, in test_max3d_1_five

    self.assertEqual(a2.max3d(1,2,3), 0)

AssertionError: 3 != 0



======================================



-------------------------------------

test_path_2_three failed.



Traceback (most recent call last):

  File "C:\Users\smish\Spring-2022\Gradingdata\Assignment2\uzrivera\a2_hidden_test.py", line 163, in test_path_2_three

    self.assertEqual(a2.path(switch_i), result)

AssertionError: None != False



======================================



-------------------------------------

test_q_1_three failed.



Traceback (most recent call last):

  File "C:\Users\smish\Spring-2022\Gradingdata\Assignment2\uzrivera\a2_hidden_test.py", line 113, in test_q_1_three

    self.assertAlmostEqual(answer[0],0.41,2)

AssertionError: -0.5857864376269049 != 0.41 within 2 places (0.9957864376269048 difference)



======================================



-------------------------------------

test_q_2_one failed.



Traceback (most recent call last):

  File "C:\Users\smish\Spring-2022\Gradingdata\Assignment2\uzrivera\a2_hidden_test.py", line 96, in test_q_2_one

    self.assertAlmostEqual(answer[0],2.5,2)

AssertionError: 3.4166666666666665 != 2.5 within 2 places (0.9166666666666665 difference)



======================================



-------------------------------------

test_q_2_two failed.



Traceback (most recent call last):

  File "C:\Users\smish\Spring-2022\Gradingdata\Assignment2\uzrivera\a2_hidden_test.py", line 103, in test_q_2_two

    self.assertAlmostEqual(answer[0],7.89,2)

AssertionError: 11.387482193696062 != 7.89 within 2 places (3.4974821936960625 difference)



======================================



-------------------------------------

test_rR_2_one failed.



Traceback (most recent call last):

  File "C:\Users\smish\Spring-2022\Gradingdata\Assignment2\uzrivera\a2_hidden_test.py", line 238, in test_rR_2_one

    self.assertAlmostEqual(funcresult, occupancyOutput[i], 2)

AssertionError: 98 != 98.21 within 2 places (0.20999999999999375 difference)



======================================



-------------------------------------

test_rR_3_two failed.



Traceback (most recent call last):

  File "C:\Users\smish\Spring-2022\Gradingdata\Assignment2\uzrivera\a2_hidden_test.py", line 245, in test_rR_3_two

    self.assertAlmostEqual(a2.r(i), r, 2)

AssertionError: 74 != 74.01234567901234 within 2 places (0.012345679012341293 difference)



======================================



Code tests: 37.0/50.0

g: 5/5

f: 5/5

h0: 1/1

h1: 1/1

h: 3/3

q: 0/5

eq: 5/5

path: 3/5

max2d: 3/3

max3d: 4/5

rectangle: 5/5

box: 2/2

rR: 0/5

