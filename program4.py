"""Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""
a=int(input("Enter your age:= "))
if a<=10:
  print("kid")
elif a<=20:
  print("Teen")
elif a<=40:
  print("young")
elif a<=60:
  print("Experienced")
elif a>=60:
  print("citizen")        
