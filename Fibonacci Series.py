num=int(input("Enter the Value :"))
previous=0
present=1                       # present+previous # 0+1=1
sum=0
if num < 0 :
  print("Enter the positive number !")
elif num == 1 :
  print("The fabibonacci series of ",num, "is :",previous)
else:
  while sum < num:
    print(previous)
    fib=present+previous
    previous=present
    present=fib
    sum=sum+1
