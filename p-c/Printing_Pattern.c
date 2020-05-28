/*
In this problem, you need to print the pattern of the following form containing the numbers from  to .

                            4 4 4 4 4 4 4  
                            4 3 3 3 3 3 4   
                            4 3 2 2 2 3 4   
                            4 3 2 1 2 3 4   
                            4 3 2 2 2 3 4   
                            4 3 3 3 3 3 4   
                            4 4 4 4 4 4 4   

*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int num;
    int i=0;
    int j=0;
    int k=0;
    int a=0;

scanf("%d", &num);

k=num;

int cont=0;

int valores[50][50];
do
{
for(i=cont;i<2*num-cont-1;i++)
  { 
    for(j=cont;j<2*num-cont-1;j++)
    { 
    if(i==a||j==a||i==num*2-a-2||j==num*2-a-2)
      valores[i][j]=k;
    }
  }
  cont++;
 k--;
 a++;
 }
 
 while(k>0);
      for(i=0;i<num*2-1;i++)
        {
        for(j=0;j<num*2-1;j++)
        {
             printf("%d ",valores[i][j]);
        }
 printf("\n");
 }



}