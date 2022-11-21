"""Write a python program to check whether a given string is a multiword string or single
word string using match case statement"""


a=len(str(input("enter the string:= ")))
match a:
  case 1:
    print("single")
  case _:
    print("multiple")
  

