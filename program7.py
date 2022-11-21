"""Write a python program to check whether a given number is positive, negative or
zero using match case statement"""


num=int(input("enetr a no "))
match num:
  case num if num>0:
    print("no is pasitive")
  case num if num<0:
    print("no is negative")
  case num if num==0:
    print("no is zero")   
  case _:
    print()      