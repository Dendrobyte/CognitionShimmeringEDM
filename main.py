# Gather Input
posValInput = input("Please paste the number of degrees for the POSITIVE rotation data, separated by SPACES\n")
posVals = posValInput.split(" ")
negValInput = input("Please paste the number of degrees for the NEGATIVE rotation data, separated by SPACES\n");
negVals = negValInput.split(" ")

# Could be genuine mistake so we make sure they are the same length
if(len(posVals) != len (negVals)):
  print("Please note: The length of positive data and negative data arrays are different. You should make sure they are the same length! Exiting Program...")
  exit()

print("---- Input Gathered! ----")

# How much data do they want
numberAmt = len(posVals)

# Enter an int, not going to worry about input error
returnDataNum = input("How many new data points would you like? Existing sample size: " + len(posVals) + "\n")
print("---- Printing " + returnDataNum + " New Data Points... ----\n")

import random

for i in range(returnDataNum):
  posRand = random.randint(len(numberAmt));
  negRand = random.randint(len(numberAmt));
  print(str(i) + ": " )

