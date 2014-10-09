# program to prompt for 8 numbers and report the total to the user
print("This program will add together 8 numbers and show the total")
num = 0
for count in range (8):
    num = num + int(input("Please enter the next number\n"))
print("The total is {0}".format(num))
