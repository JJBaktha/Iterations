#Jeeson Baktha
#Iteration Development Excercise 2
#5 October 2014

program = 1

while program == 1:
    num_stars = int(input("Please enter the number of stars you want\n"))
    num_rows = int(input("Please enter the number of rows you want\n"))
    for count in range(num_rows):
        print("*" * num_stars)
