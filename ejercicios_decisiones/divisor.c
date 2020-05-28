#include <stdio.h>
/*
Program a code in C, given two integers that enter as data, indicate if one is a divisor of the other.

*/
int main()
{
    int num1;
    int num2;//Variables

    printf("Introduzca el primer número: ");
    scanf("%d", &num1); //indica sin signo
    printf("Introduzca el segundo número: ");
    scanf("%d", &num2); //indica sin signo


    if (num1 >= num2)
    {
    if (num1  % num2 == 0)
    {
    printf("Es divisor %d de %d\n", num1,
    num2);
    }
    else
    printf("%d no es divisor de %d\n", num2,num1);
    }
       
    else
    printf(" %d No es divisor porque  %d\n es mayor ",num1,num2);
    
    
    // numero alrevez
    
    if (num1 <= num2)
    {
    if (num2  % num1 == 0)
    {
    printf("Es divisor %d de %d\n", num2,
    num1);
    }
    else
    printf("%d no es divisor de %d\n", num1,num2);
    }
       
    else
    printf(" %d No es divisor porque es mayor %d\n",num1,num2);
    
    


}