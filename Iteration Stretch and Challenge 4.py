#Jeeson Baktha
f = input("Please enter a sentence and this program will count the number of words in it\n")

wordcount=0
for lines in f:
         f1=lines.split()
         wordcount=wordcount+len(f1)
print (wordcount)

