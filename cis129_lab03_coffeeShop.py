# INPUTS for the user

nbrOfCoffee = int(input('Enter Number of Coffee: '))
nbrOfMuffin = int(input('Enter Number of muffins: '))
nbrOfWater = int(input('Enter Number of waters: '))
nbrOfDoughnuts = int(input('Enter Number of doughnuts: '))

# PROCESSING
# Constant variables

priceOfWater = 2
priceOfDoughnut = 6
priceOfCoffee = 5
priceOfMuffin = 4
Tax = 0.06

# Calculations
Subtotal_Water = priceOfWater * nbrOfWater
Subtotal_Doughnut = priceOfDoughnut * nbrOfDoughnut
Subtotal_Muffin = priceOfMuffin * nbrOfMuffin 
Subtotal_Coffee = priceOfCoffee * nbrOfCoffee
Subtotal = nbrOfCoffee * priceOfCoffee + nbrOfMuffin * priceOfMuffin + nbrOfDoughnut * priceOfDoughnut + nbrOfWater * priceOfWater
TaxOfSubtotal = Subtotal * Tax

# The users final total

GrandTotal = TaxOfSubtotal + Subtotal

# OUTPUT- print statments

print('************************************************************ ')
print('Derek\'s Coffee and Muffin Shop')
print(nbrOfDoughnut,'Doughnuts at $6 each: $',Subtotal_Doughnut)
print(nbrOfWater,'Waters at $2 each: $',Subtotal_Water)
print(nbrOfCoffee,'Coffee at $5 each: $',Subtotal_Coffee)
print(nbrOfMuffin,'Muffins at $4 each: $',Subtotal_Muffin)
print('6% Tax: $',TaxOfSubtotal)
print('-------------')
print('Total: $',GrandTotal)
print('************************************************************')
