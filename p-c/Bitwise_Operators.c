/*
Task
Given set , find:

the maximum value of  which is less than a given integer , where  and  (where ) are two integers from set .

the maximum value of  which is less than a given integer , where  and  (where ) are two integers from set .

the maximum value of  which is less than a given integer , where  and  (where ) are two integers from set .

Input Format

The only line contains  space-separated integers,  and , respectively.
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void max(int n, int k) {
  //Write your code here.
int x=0;
int y=0;
int z=0;
int a,b,c;
for(int i=1;i<=n;i++)
{
    for(int j=i+1;j<=n;j++)
    {
        a=i|j;
        b=i&j;
        c=i^j;
        if(a<k)
        {
            if(y<a)
            y=a;
           // print(y);
        }
        if(b<k)
        {
            if(x<b)
            x=b;
             // print(x);
        }
        if(c<k)
        {
            if(z<c)
            z=c;
             // print(z);
        }
    }
}
printf("%d\n%d\n%d",x,y,a);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    max(n, k);
 
    return 0;
}