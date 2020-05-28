/*
C For Loop: Exercise-35 with Solution
Write a program in C to display the first n terms of Fibonacci series. The series is as follows:
Fibonacci series 0 1 2 3 5 8 13 .....
*/

#include <stdio.h>

int main()
{
   int val1=0;
   int val2=1;
   int temporal;
   int i,num;
   printf("Input number of terms to  display : ");
   
   scanf("%d",&num);
  
 
  for(i=1;i<=num;i++)
   {
     temporal=val1+val2;
     printf("%d ",temporal);
     val1=val2;
     val2=temporal;
   }
   printf("\n");
}