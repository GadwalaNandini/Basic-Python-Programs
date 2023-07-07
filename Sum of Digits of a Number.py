def getsum(n):
  sum=0
  for digit in str(n):
    sum=sum+int(digit)
  return sum
n=input("Enter the Value: ")
print(getsum(n))


# withou using a function
num=input("Enter the Value: ")           #1+2+3=6
count=0
for i in str(num):
  count=count+int(i)
print("Value : ",count)
