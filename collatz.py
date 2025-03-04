#collatz.py
#Program that asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd,
#multiply it by three and add one.
#Have the program end if the current value is one.
#Author: Siobhán Maher

numbers = [] # to hold a list of numbers after each answer is returned

number = int(input("Enter a positive number - even will be divided by 2, odd muliplied x 3 + 1, enter your number NOW: "))  # asks user to enter a positive integer + explains
                                                                                                                            # what the programme will do

while number != 1: # while the answer is not equal to 1, do the following tasks

    if (number % 2) == 0: # check if the number is even (i.e. there is no remainder when divided by 2 which means it is even)
        number = number // 2 # if the number is even then divide it by two, floor division gets rid of answers like 17.0, 11.0 and replaces with 17, 11 
                            # I read about this here: https://www.geeksforgeeks.org/floor-division-in-python/

        print(f"the number is {number};  if even divide by 2, if odd muliply x 3 + 1, unless the answer is 1...") # print "the number is" and the value of the number

    else: # if the number isn't even, then do the following
        number = (number*3) + 1 # multiply the number by 3 and add 1
        print(f"the number is {number};  if even divide by 2, if odd muliply x 3 + 1, unless the answer is 1...") # print the number is
   
    if number == 1: # if the answer equals to 1
        print ("... because 1 is the final number and it ends this program...THE END") # programme will stop now as while loop is now = 1 and !=1 no longer true
    numbers.append(number) # adds each new number to the list
    print (numbers) # prints the list of numbers that have been returned so far