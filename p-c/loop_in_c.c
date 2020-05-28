/*
For each integer  in the interval  (given as input) :

If , then print the English representation of it in lowercase. That is "one" for , "two" for , and so on.
Else if  and it is an even number, then print "even".
Else if  and it is an odd number, then print "odd".
Input Format

The first line contains an integer, .
The seond line contains an integer, .

*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main() {

int a, b;


scanf("%d\n%d", &a, &b);
char *numeros[] = {"one", "two", "three", "four", "five", "six", "seven",  "eight",  "nine", "even", "odd"};
   //int letras;
  for (int i=a; i<=b; i++) {
    if (i <= 9) 
    printf ("%s\n", numeros[i-1]);
    else 
    printf ("%s\n", numeros[9+(i%2)]);


}
// Complete the code.

return 0;
}
