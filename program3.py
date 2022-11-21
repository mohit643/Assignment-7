"""
Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.

"""
a=int(input("enter the side of tringle "))
b=int(input("enter the side of tringle "))
c=int(input("enter the side of tringle "))


if a==b==c:
  print("equilateral Tringle")  
elif a==b:
  print("isosceles Tringle")  
elif a**2+b**2==c:
  print("Right angle Tringle")
else:
  print("not a tringle")    
