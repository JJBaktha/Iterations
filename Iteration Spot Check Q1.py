#Jeeson Baktha
#Iteration spot check Question 1
#12 November 2014

number = 0
total = 0

while number != -1:
    number = int(input("Please enter a number (or enter -1 when you are done)\n"))
    total = (number * number) + total - 0.5
print("The total is {0}".format(total))

