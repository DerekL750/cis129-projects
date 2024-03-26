# The following code is Pseudocode
# Please convert the following code to Python Code and save as Lab6.py
import math
# main module                                 
def main():
   # Local variable for the total number of hot dogs needed.
    total = 0

   # Input --------------------------------------
   # Get the total number of hot dogs needed.
    total = getTotalHotDogs()

   # Processing ----------------------------------
   # Named constants for the package sizes
    DOGS = 10   # Hot dogs in a package
    BUNS = 8    # Hot dog buns in a package

   # Local variables
    dogsLeft = 0 # Left over hot dogs
    bunsLeft = 0 # Left over hot dog buns
    minDogs = 0  # Minimum packages of hot dogs
    minBuns = 0  # Minimum packages of hot dog buns

   # Calculate the number of left over hot dogs.
    dogsLeft = (DOGS - total % DOGS) % DOGS

   # Calculate the minimum number of packages of hot dogs.
    minDogs = math.ceil(total / DOGS) 

   # Calculate the number of left over hot dog buns.
    bunsLeft = (BUNS - total % BUNS) % BUNS

   # Calculate the minimum number of packages of hot dogs buns.
    minBuns = math.ceil(total / BUNS) 

   # Output ----------------------------------------
   # Display the results.
    ShowResults(dogsLeft, minDogs, bunsLeft, minBuns)


# The getTotalHotDogs module gets the number of people
# attending the cookout and the number of hot dogs each
# person will be given, and stores the product in the
# totalHotDogs reference variable.

def getTotalHotDogs():

   # Local variables
   people = 0   # Number of people attending
   hotDogs = 0  # Hot dogs per person

   # Get the number of people attending the cookout.
   people = int(input(print("Enter the number of people attending the cookout: ")))

   # Get the number of hot dogs each person will be given.
   hotDogs = int(input(print(" Enter the number of hot dogs for each person: ")))

   # Calculate the total number of hot dogs needed.
   total = people * hotDogs
   return total

# The showResults module accepts the total number of hot dogs
# as an argument and calculates the minimum packages of hot
# dogs and hot dog buns, the left over hot dogs and hot dog
# buns, and displays the results.

def ShowResults(dogsLeft, minDogs, bunsLeft, minBuns):

   # Display the minimum packages of hot dogs needed.
   print("Minimum packages of hot dogs needed: ", minDogs)

   # Display the minimum packages of buns needed.
   print("Minimum packages of hot dog buns needed: ", minBuns)

   # Display the number of hot dogs left over.
   print("Hot dogs left over: ", dogsLeft)

   # Display the number of hot dog buns left over.
   print("Hot dog buns left over: ", bunsLeft)

main()