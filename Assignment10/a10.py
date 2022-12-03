# Before submitting to the Autograder, please comment the import statements for matplotlib (line 9 and 10): 
# These are libraries/packages that are required to draw the graphical plot and you can use them
# for testing while you work on the HW, but comment these lines and the entire code for graphit() function
# before submitting to the Autograder.

import numpy as np
import matplotlib.pyplot as plt
import random as rn
import math 
import sqlite3
import os

########################
#PROBLEM 1
########################
# translates a random int into a step along the random walk
# parameters: int i for the step index, numpy array x for tracking the left/right location at index i,
# numpy array y for tracking the forward/backward location at index i.
# return: None

def step(i, x, y):
    
    direction = rn.randint(1,4)
    
    # Take the step based on the randomly selected direction 
    # TODO: implement this function
    
    pass


# Do Not Modify this function. It creates the plot to show
# the random walk (as shown in the HW PDF). Once you complete
# the step() function, and run this file, you will see a plot
# similar to HW PDF which will show the random walk generated by your code.
# Make sure that after you are done testing, you comment the call to this function
# under the __name__ == "__main__". If you call this function and submit to the Autograder, it
# may return unexpected errors because Autograder does not support graphical plots yet.

def graphit(x,y,n):
   
    plt.title("Random {0} Walk\nLast Location {1},{2}".format(n, int(x[n-1]),int(y[n-1])) )
    plt.plot(x,y) 
    plt.plot([x[1],x[1]],[y[1]-10,y[1]+10], "b-")
    plt.plot([x[1]-10,x[1]+10],[y[1],y[1]], "b-")
    plt.plot([x[n-1]-10,x[n-1]+10],[y[n-1],y[n-1]], "r-")
    plt.plot([x[n-1],x[n-1]],[y[n-1]-10,y[n-1]+10], "r-")
    plt.show() 


###############
# PROBLEM Two
###############

class Vector:
    def __init__(self, *x):
        self.__v = x

    def get_tuple(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rmul__(self, other):
            return self.__mul__(other)

    def __mul__(self, other):
        if type(other) in (int, float):
             return Vector(*(i*other for i in self.__v))
        else:
            return round(sum([i*j for i,j in zip(self.__v, other.get_tuple())]), 3)

    def __abs__(self):
        pass

    def __neg__(self):
        pass

    def __eq__(self, other):
        pass

    def __repr__(self):
        return str(self.__v).replace("(","<").replace(")",">")


# if you want to fix where the db is
# os.chdir("c:path+filename")

# connection = sqlite3.connect("mydatabase.db")
# my_cursor = connection.cursor()

#############################################
## RUN THE FOLLOWING ONLY ONCE 
# If you create the table again then SQL will throw and error
# that TABLE already exist. To prevent that, create the table only once
# and comment the code back.

## First create the table
# my_cursor.execute("")

## Insert values into the table
# my_cursor.execute("")
# my_cursor.execute("")
# my_cursor.execute("")
# my_cursor.execute("")
# my_cursor.execute("")
# my_cursor.execute("")

#############################################


if __name__ == "__main__":
    ''' uncomment as needed '''
    
    # # PROBLEM 1
    # # number of steps (n)
    # # You should change the number of steps to see
    # # to see how it affects the plot
    # n = 100000    
    # x = np.zeros(n) 
    # y = np.zeros(n) 

    # # fill array with step values 
    # for i in range(1, n):
    #     step(x,y,i)

    # # The following line will call graphit() function which will 
    # # create a graphical plot for you.
    # # Before submitting to the Autograder-make sure that you comment this line, 
    # # because the Autograder can't create graphical output yet.
    
    # # graphit(x,y,n)

    # # PROBLEM 2      
    # x,y,w = Vector(1,2), Vector(3,-1), Vector(*(10,10))  
    # z,a = Vector(0,3,2),Vector(-1,-1,-1) 
    # print(x,y,z,a)
    # print(x+y,z+a)
    # print(x*y,z*a)
    # print(5*x,5*z)
    # print(abs(x),abs(z))
    # print(-x,-z)
    # print(x - y + y == x, 2 * z == z + z)

    # # PROBLEM 3
    # data = [('Phoenix', 'Arizona', 105, 90),('Tucson', 'Arizona', 101, 92),
    #         ('Flag Staff', 'Arizona', 105, 90), ('San Diego', 'California', 77, 60),
    #         ('Alguquerque', 'New Mexico', 80, 72), ('Nome', 'Alaska', 64 ,-54)]   

    # # QUERY 1 Select all records from the database
    # print("Query 1")
    # for i in my_cursor.execute("SELECT * FROM Weather"):
    #     print(i)
    # print("List Comprehension: ", data)

    # # QUERY 2 
    # # Select all the records from the database where the high temperature is less than 80
    # print("\nQuery 2")
    # for i in my_cursor.execute(""):
    #     print(i)
    # print("List Comprehension: ", [d for d in data if d[2] < 80 ])


    # # QUERY 3 
    # # Select All the cities where the low temperature is greater than the low of Albuquerque 
    # print("\nQuery 3")
    # for i in my_cursor.execute(""):
    #     print(i)
    # print("List Comprehension: ",[d[0] for d in data if d[3] > [d[3] for d in data if d[0] == 'Alguquerque'][0]])


    # # QUERY 4 
    # # Select the city and temperature with the smallest low temperature 
    # print("\nQuery 4")
    # for i in my_cursor.execute(""):
    #     print(i)
    # print("List Comprehension: ",[(d[0],d[3]) for d in data if d[3] in (sorted(data, key = lambda x:x[3])[0])])


    # # QUERY 5 
    # # Select the city temperature with the largest high temperature 
    # print("\nQuery 5")
    # for i in my_cursor.execute(""):
    #     print(i)
    # print("List Comprehension: ",[(d[0],d[2]) for d in data if d[2] in (sorted(data, key = lambda x:x[2],reverse=True)[0])])


    # # QUERY 6 
    # # Display the average High and Low temperatures
    # # You are not allowed to use Avg()
    # print("\nQuery 6")
    # for i in my_cursor.execute(""):
    #     print(i)
    # print("List Comprehension: ", [(sum([d[2] for d in data])/len(data),sum([d[3] for d in data])/len(data))])


    # # QUERY 7 
    # # Give the counts of cities by their Low temperatures
    # print("\nQuery 7")
    # for i in my_cursor.execute(""):
    #     print(i)
    # print("List Comprehension: ", [(i,list(map((lambda x: x[3]),data)).count(i)) for i in set(map((lambda x: x[3]),data))])

    # connection.close()