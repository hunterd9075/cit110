# CTI-110-2B01 
# P2HW2 - Tip Tax Total 
# DeOnna Hunter
# April 22, 2018


FoodCost=float(input ("Enter Cost of meal: $ " ))

TipAmount=(0.18* FoodCost)
print("The amount of your tip should be: $ ",TipAmount)

SalesTax=0.07 * FoodCost
print ("The amount of sales tax is: $ ",SalesTax )

TotalCost=FoodCost+ TipAmount+SalesTax 
print ("The total cost of your meal is: $ ",TotalCost )


print ("Thank you for your patronage. Please come again!")
