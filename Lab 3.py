# INPUTS for the user

nbrOfCoffee = int(input('Enter Number of Coffee: '))
nbrOfMuffin = int(input('Enter Number of muffins: '))

# PROCESSING
# Constant variables

priceOfCoffee = 5
priceOfMuffin = 4
Tax = 0.06

# Calculations

Subtotal_Muffin = priceOfMuffin * nbrOfMuffin 
Subtotal_Coffee = priceOfCoffee * nbrOfCoffee
Subtotal = nbrOfCoffee * priceOfCoffee + nbrOfMuffin * priceOfMuffin
TaxOfSubtotal = Subtotal * Tax

# The users final total

GrandTotal = TaxOfSubtotal + Subtotal

# OUTPUT- print statments

print('************************************************************ ')
print('Derek\'s Coffee and Muffin Shop')
print(nbrOfCoffee,'Coffee at $5 each: $',Subtotal_Coffee)
print(nbrOfMuffin,'Muffins at $4 each: $',Subtotal_Muffin)
print('6% Tax: $',TaxOfSubtotal)
print('-------------')
print('Total: $',GrandTotal)
print('************************************************************')
