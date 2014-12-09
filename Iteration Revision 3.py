#Jeeson Baktha
#Iteration Revision 3
#12 November 2014

print("This program will average the amount of numbers you have entered")

user_range = int(input("Please enter the amount of numbers you want averaged\n"))
num = 0
for count in range (user_range):
                 num = num + int(input("Please enter another number\n"))
average_num = num / user_range

print("This is the average of the total of the numbers you have enteres above: {0}".format(average_num))
                 
