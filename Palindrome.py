word=input("Enter the string : ")
r_word=word[::-1]                          # reverse 
if r_word==word:
  print("Palindrome")
else:
  print("Not Palindrome")
