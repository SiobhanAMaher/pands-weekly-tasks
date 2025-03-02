#accounts.py
#Modify the program ACCOUNTS.PY to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
#author: Siobhán Maher

bank=int(input('Your bank account - no limit on number: ')) # asks for digit integer input
b = str(bank) # converts integer to string so replace can be used
print(b.replace(b[0:-4],"XXXXXX")) # replaces all digits before the last four with XXXXXX