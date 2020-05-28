/*6. Write a program in C to display the multiplication table of a given integer. Go to the editor
Test Data :
Input the number (Table to be calculated) : 15
Expected Output :
15 X 1 = 15
...
...
15 X 10 = 150*/
#include <stdio.h>
int main()
{
   int i=0;
   int num=0;; 
   int mult=1;   
   printf("Input the number (Table to be calculated) :");    
   scanf("%d",&num);
      


   for(i=1;i<=10;i++)
   {
  
      mult=num*i;
        
	   printf("%d X %d = %d \n",num, i,mult);
     	//printf("%d", num);
	//printf("\n");
   }
}