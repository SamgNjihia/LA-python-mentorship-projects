year = int(input("please Enter year: "))
checkRemainder = year % 4
checkCentuary1 = year % 100
checkCentuary2 = year % 400

if checkRemainder == 0 and checkCentuary1 != 0:
  
  print(f"{year} is a Leap Year")

elif checkCentuary1 == 0 and checkCentuary2 == 0:

  print(f"{year} is a Leap Centuary Year" )

else:

  print(f"{year} is not a Leap Year")