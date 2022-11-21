# Write a python script to display the number of days in a given month numbe


month = int(input("Enter month "))
match month:
      case month if month in (1,3,5,7,8,10,12):
            print("31 days on this ",month,"month")
      case month if month in (4,6,9,11):
            print("30 days on this month")
      case month if month == 2:
            print("28 days on this month")
      case _:
            print("invalid month no ")                  
