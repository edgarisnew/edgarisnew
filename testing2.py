greeting = "Hello"
#insert your name here
name = "Edgar"

x = ""

message = f"""{greeting}, {name}. 
Welcome!"""

print(message)
print(x)
print("Please remember: taxes have to be typed as 0.x and not a full number or a percentage.")
print(x)
#insert your yearly income here
print("Yearly Income Before Taxes:")
yearly_income = 100000
print(x)
print(yearly_income)
print(x)
#insert your taxes here
print("Taxes:")
print(x)

#taxes must be presented in the following way: 0.x 
taxes = 0.3

print(taxes)
print(x)


print("Yearly Income After Taxes")
print(x)


taxes_bracket = 1-taxes

yearly_after = yearly_income * taxes_bracket

if taxes<0 or taxes>1:
   print("ERROR: Taxes cannot be under or above 1")

else:
  print(yearly_after)

print(x)


  