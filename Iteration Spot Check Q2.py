#Jeeson Baktha
#Iteration Spot check Q2
#12 November 2014

print("This program will produce a times table (from 1 times to 12 times) for a number you input")

user_num = int(input("Please enter an interger\n"))

times_table = 0
for count in range  (1,13):
    times_table = times_table + 1
    total = times_table * user_num
    print("{0} * {1} = {2}".format(times_table, user_num, total))
