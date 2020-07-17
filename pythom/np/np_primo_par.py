#numbers prime and parer
import numpy as np

num = int (input('Enter number:'))
 

  #we check if it's a cousin
results = not np.any([num% i == 0 for i in range(2, num)])
#we check if it is even
results2 = np.any ([num% 2 == 0])
if results == True:
     print ('Yes, is prime')
 
#If not prime, you get the numbers by which it is dibible
else:
     print ('Not prime')
     for j in range (2, num):
         if num% j == 0:
             print ('Is divisible by', j)
# odd or even validation
if results2 == True:
     print ('Yes, is even')
else:
   print ('Yes, it is odd!')