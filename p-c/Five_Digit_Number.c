/*Task

In this challenge, you have to input a five digit number and print the sum of digits of the number.*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(){
    int n, val=0;
    scanf("%d", &n);
    while(n>0){
        val+=n%10;
        n/=10;
    }
    printf("%d", val);
    
    return 0;

}