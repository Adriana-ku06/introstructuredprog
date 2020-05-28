#Task
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird


num = int(input()) 
n = num % 2 

if n == 0 and (2<= num <=5): 
    print('Not Weird')
elif n == 0 and (6<= num <=20): 
    print('Weird')
elif n == 0 and num > 20: 
    print("Not Weird")
elif num % 2 != 0: 
    print('Weird')