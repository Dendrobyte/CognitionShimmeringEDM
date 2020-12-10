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
returnDataNum = input("How many new data points would you like? Must be a number!\nExisting sample size: " + str(len(posVals)) + "\n")
print("---- Printing " + returnDataNum + " New Data Points... ----\n")

import random

newPosVals = []
newNegVals = []
for i in range(int(returnDataNum)):
  posRand = random.randint(0, numberAmt)-1;
  negRand = random.randint(0, numberAmt)-1;
  randPosVal = posVals[posRand]
  randNegVal = negVals[negRand]
  newPosVals.append(randPosVal)
  newNegVals.append(randNegVal)
  print(str(i) + ": RandomPositiveDegree is [" + randPosVal + "] and RandomNegativeDegree is [" + randNegVal + "]")

print("Pos vals: " + str(newPosVals))
print("Neg vals: " + str(newNegVals))
print("---- Complete ----\n")
