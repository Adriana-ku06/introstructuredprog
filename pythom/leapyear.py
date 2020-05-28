#adriana ku
print ("Introdusca un rango de años")
print ("Año de inicio")
startYear = int(input())
print ("Año final")
endYear = int(input()) 
##print ("leap years:")

for year in range(startYear, endYear):
  
  if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
    print ('{} is leap year'.format(year))