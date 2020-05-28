/*5. Write a program in C to display the cube of the number upto given an integer. Go to the editor
Test Data :
Input number of terms : 5
Expected Output :
Number is : 1 and cube of the 1 is :1
Number is : 2 and cube of the 2 is :8
Number is : 3 and cube of the 3 is :27
Number is : 4 and cube of the 4 is :64
Number is : 5 and cube of the 5 is :125*/

#include <stdio.h>
#include <stdlib.h>
int main(void){
   int i=0;
   int num=0;
  int cube=0;
  int j=0;

    
    printf("Input number of terms : ");
    scanf(" %d", &num);
   
   for(i=1;i<=num;i++){
     cube=i;
        for(j=1;j<=2;j++){
          
          cube=cube*i;
           
          } 
         // printf("%d", cube);  

        printf("\n Number is : %d and cube of the %d is :%d",i, i, cube);  
       
       
   }
  
}