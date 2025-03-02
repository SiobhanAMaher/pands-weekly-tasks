#accounts.py
#programme which asks user to enter integer amounts and that reads in a 10 character account number 
#and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
#author: Siobhán Maher

bank=int(input('Your ten digit bank account: ')) # asks for 10 digit integer input, error if non numeric characters used
b = str(bank) # converts integer to string so len function can be used as cannot use len on integer
length = len(b)
if length < 10: 
    print ("ERROR - MUST BE 10 CHARACTERS") # if the length is less than 10 characters, give user an error
if length > 10:
    print ("ERROR - MUST BE 10 CHARACTERS") # if the length is greater than 10 characters, give user an error
if length == 10:
   print(b.replace(b[0:6],"XXXXXX")) # if length is = 10 print string with first 6 digits replaced by XXXXXX
   #combined "Slice from Start" + Replace String from pands 3.2 video to see if it would work and it did!
   