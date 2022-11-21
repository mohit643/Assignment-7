"""Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number"""

a=int(input("enter the no:= "))
if a%2==0:
  print("Saurabh shukla")
elif a%2!=0 and a<0:
  print("Prateek jain")
elif a%2!=0 and a>=0:
  print("Aditya choudhary")    