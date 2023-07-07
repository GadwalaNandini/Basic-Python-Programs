num=20
if num<0:
  print("Enter the positive number!")
else:
  sum=0
  while(num > 0):
    sum=sum+num        # 20+0 , 20+1 .......
    num=num-1           # 20+19 , 20+19+18 ......
  print("The sum is",sum)
