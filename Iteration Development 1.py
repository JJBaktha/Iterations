#Jeeson Baktha
#Iterations Stretch and Challenge
#16 October 2014

number = int(input("Enter a non-negative integer to take the factorial of: "))

product = 1

for count in range(number):
    product = product * (count + 1)

print(product)
