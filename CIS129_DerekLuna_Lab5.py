# Module 5 Lab-5
# Derek Luna
# 3/10/24
# This program will ask the user the number of bottles returned in a weeks worth of data
# and will give the user the total paid out and the total bottles. the program will stop if they answer no

# Declare variables

totalbottles = 0 #stores the accumulated bottle values
counter = 1      #variable will control the loop
todaybottles = 0 #this variable stores the number of bottles returned
totalpayout = 0  #this variable stores the calculated value of totalbottles times .10
Keepgoing = "y"  #this is used to run the program again
# Loop to run program again

while Keepgoing == "y" :
    # getbottles code
    NBR_OF_DAYS = 7
    totalbottles = 0
    todaybottles = 0
    counter = 1
    while counter <= NBR_OF_DAYS :
        # calcPayout code
        todaybottles = int(input(f"Enter number of bottles returned for day #{counter} : "))
        totalbottles += todaybottles 
        counter = counter + 1
    #calcPayout code
    PAYOUT_PER_BOTTLE = .10
    totalpayout = totalbottles * PAYOUT_PER_BOTTLE 
    # printInfo code
    print(f'The total number of bottles collected is {totalbottles}')
    print(f'The total paid out is ${totalpayout.3f}')
    print("Do you want to enter another week's worth of data?")
    keepgoing = (input("(Enter y or n): ")) 
    if keepgoing == "n":
            break
   