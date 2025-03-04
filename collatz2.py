#collatz2.py - MODIFIED TO PRINT JUST THE LIST and not every line
#Program that asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd,
#multiply it by three and add one.
#Have the program end if the current value is one.
#Author: Siobhán Maher

numbers = [] # to hold a list of numbers after each answer is returned

number = int(input("Enter a positive number - even will be divided by 2, odd muliplied x 3 + 1 until answer of 1 achieved; ENTER your number NOW: "))  # asks user to enter a positive integer + explains
                                                                                                                            # what the programme will do


while number != 1: # while the answer is not equal to 1, do the following tasks
    numbers.append(number) # adds each new number to the list
    if (number % 2) == 0: # check if the number is even (i.e. there is no remainder when divided by 2 which means it is even)
        number = number // 2 # if the number is even then divide it by two, floor division gets rid of answers like 17.0, 11.0 and replaces with 17, 11 
                            # I read about this here: https://www.geeksforgeeks.org/floor-division-in-python/


    else: # if the number isn't even, then do the following
        number = (number*3) + 1 # multiply the number by 3 and add 1

print (numbers) # prints the list of numbers that have been returned so far
        