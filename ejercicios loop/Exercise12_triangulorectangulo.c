
/*
Exercise-12 with Solution
Write a program in C to make such a pattern like right angle triangle with number increased by 1.
The pattern is as follows :

   1
   2 3
   4 5 6
   7 8 9 10

*/
#include <stdio.h>
#include <stdio.h>
int main()
{
   int i=0;
   int j=0;
   int filas,num=1;
   
    
   printf("Input number of rows : ");    
   scanf("%d",&filas);
       //num=1;


   for(i=1;i<=filas;i++)
   {
   //num=1;
	for(j=1;j<=i;j++)
        
	   printf("%d ",num++);
     	//printf("%d", num);
	printf("\n");
   }
}
