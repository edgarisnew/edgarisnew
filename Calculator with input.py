greeting = "Hello"
#insert your name here
name = input("What is your name?")

x = ""

message = f"""{greeting}, {name}. 
Welcome!"""

print(message)
print(x)
print("Please remember: taxes have to be typed as 0.x and not a full number or a percentage.")
print(x)
#insert your yearly income here
yearly_income = int(input("What is your yearly income?"))
print(x)
print(yearly_income)
print(x)
#insert your taxes here
#taxes must be presented in the following way: 0.x 
taxes = input("Whats the tax rate in your country?")

taxes_b = 1-float(taxes)

print(taxes)
print(x)


print("Yearly Income After Taxes")
print(x)



yearly_after = yearly_income * taxes_b

if int(float(taxes))<0 or int(float(taxes))>1:
   print("ERROR: Taxes cannot be under or above 1")

else:
  print(yearly_after)

print(x)

