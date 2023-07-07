num=4
fact=1
if num < 0:
  print("We Can't get a factorial try Positive Values!")
elif num==0:
  print("The factorial of Zero is 1!")
else:
  for i in range(1,num+1):
    fact=fact*i
  print("The factorial of",num,"is",fact)
