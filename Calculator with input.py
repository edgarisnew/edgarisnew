greeting = "Hello"
#insert your name here
name = input("What is your name?")

x = ""

message = f"""{greeting}, {name}. 
Welcome!"""

print(message)
print(x)
print("Please remember: taxes have to be typed as a full number without the percentage symbol.")
print(x)
#insert your yearly income here
yearly_income = int(input("What is your yearly income?"))
print(x)
print(yearly_income)
print(x)
#insert your taxes here
taxes = input("Whats the tax rate in your country?")

taxes_b = int(taxes) / 100

print(taxes)
print(x)


print("Yearly Income After Taxes")
print(x)



yearly_after = yearly_income * taxes_b

if float(taxes)<0 or float(taxes)>100:
   print("ERROR: Taxes cannot be under or above 100")

else:
  print(yearly_after)

print(x)

