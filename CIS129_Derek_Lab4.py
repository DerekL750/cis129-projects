# Module 4 Lab-4
# Derek Luna
# 2/26/24
# This program collects the input of monthly sales and the sales percent increase from the user and gives the user a bonus amount and a store bonus amount

# declare local variables

monthlysales = 0 #monthly sales amount
storeAmount = 0 #store bonus amount
empAmount = 0 #employee bonus amount
salesIncrease = 0 #percent of sales increase
prompt = 'Enter monthly sales: '

# This code gets the monthly sales

monthlysales = float(input(prompt))  #code gets monthly sales

# this code determines the store bonus

if monthlysales >= 110000 :
        storeAmount = 6000
elif monthlysales >= 100000 :
        storeAmount = 5000
elif monthlysales >= 90000 :
        storeAmount = 4000
elif monthlysales >= 80000 :
        storeAmount = 3000
else: storeAmount = 0

# this code gets the percent of increase in sales

salesIncrease = float(input('Enter sales increase percent:'))
salesIncrease = salesIncrease / 100

# This code determines the employee bonus

if salesIncrease >= .05 :
        empAmount = 75
elif salesIncrease >= .04 :
        empAmount = 50
elif salesIncrease >= .03 :
        empAmount = 40
else: empAmount = 0

# This code prints the bonus information

print("the store bonus amount is $", storeAmount)
print("the employee bonus amount is $", empAmount)
if (storeAmount  == 6000) and (empAmount == 75) :
        print('congrats! you have reached the highest bonus amount possible! ')