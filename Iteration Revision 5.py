#Jeeson Baktha
#Iteration Revision 5
#12 November 2014

print("This program will find the average of the amount of nubers you enter")

count = 0
total_num = 0

first_question = input("Do you want to enter a number? Type yes if u do or -1 if u dont\n")

while first_question == "yes":
    num_1 = int(input("Please enter another number\n"))
    total_num = total_num + num_1
    count = count + 1
else:
        average_num = total_num / count
print("The average is {0}".format(average_num))
    
