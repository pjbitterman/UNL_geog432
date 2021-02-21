# answers for GEOG 432/832 lab 01

# task 1: Extracts the sub-string "GIScience" from the String "Learning GIScience is awesome!"

toExtract = "Learning GIScience is awesome!"
print(toExtract[9:18])


# task 2: Uses a loop control structure to count from 0-100 by fives. The script should print the value to the console AND should print whether the value is odd or even. For example, an output could look like "15 is odd"

for i in range(0, 100, 5):
    if i % 5 == 0: # don't need this if stepping by 5, but is necessary if stepping by 1
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")

# task 3: Calculates the sum, median, and mean of the array [7, 24.5, 99, 101, 256, 128, 1000]. You must use array references or other functions in the math - do NOT directly use the numeric values in the calculation. The code should be general enough to perform the calculations for any given array. Test the same code using the array [1, 2, 3, 4, 5]. Show both results.

myArray = [7, 24.5, 99, 101, 256, 128, 1000]
mySum = 0

for i in myArray:
    mySum += i

print(mySum, "is the sum")
print(mySum / len(myArray), "is the mean")
myArray.sort()
print(myArray)
print(myArray[len(myArray) // 2], "is the median")

# also numpy stuff


# task 4: Reads the "lab01textsample.txt" file, assigns it to a variable, and then prints the file line-by-line. Extra points if you can skip printing the first 2 lines.

import os
print(os.getcwd())

f = open("./labs/lab01textsample.txt", 'r')
f.readline()
f.readline()

for line in f:
    print(line)


# task 5: Write a function that accepts as a parameter a numeric value corresponding to the **percentage score** for the class and returns the corresponding letter grade for the course. It must also return an appropriate message for scores outside of the correct range of scores. You don't have to bother with pluses or minuses, just full letter grades. Finally, test your function and show that it works for the scores: -5, 45, 70, 99, and 125.

def calculate_grade(pct_score):
    if(pct_score < 0 or pct_score > 100):
        print("your score is invalid")
    else:
        if(pct_score >= 60 and pct_score < 70):
            print("your grade is a D")
        elif(pct_score >= 70 and pct_score < 80):
            print("your grade is a C")
        elif(pct_score >= 80 and pct_score < 90):
            print("your grade is a B")
        elif(pct_score >= 90):
            print("your grade is a A")
        elif(pct_score < 60):
            print("your grade is a F")
        
calculate_grade(-5)
calculate_grade(45)
calculate_grade(70)
calculate_grade(99)
calculate_grade(125)
