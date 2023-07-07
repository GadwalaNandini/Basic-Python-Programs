string=input("Enter the String : ")         #intializing the string
count=0                                   # count variable to store the number of vowels
for i in string:                           #for loop for the string(letter by letter)
  if((i=="a" or i=="e" or i=="i" or i=="o" or i=="u") or(i=="A" or i=="E" or i=="I" or i=="O" or i=="U")):           #if condition
    count=count+1                                                 #increment of count
print("The number of Vowels are : ")
print(count)
