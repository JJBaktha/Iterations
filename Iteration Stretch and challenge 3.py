#Jeeson Baktha
#Iteration Stretch and challenge 2
#6 October 2014

multi=1
decimal=0
binary_number=input("Input Binary Number ")
for item in binary_number[::-1]:
    if item=='1':
        decimal=decimal+multi
    multi=multi*2
print(decimal)
    
                                            
