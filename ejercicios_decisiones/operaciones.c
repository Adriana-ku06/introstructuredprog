/*
Hacer un programa que lea dos n�meros, si son iguales multiplicarlos, 
si el primero es mayor que el segundo que se resten si el primero es menor que el segundo que se sumen
*/
#include <stdio.h>

int main()
{
    int num1;
    int num2;//Variables

    printf("Introduzca el primer n�mero: ");
    scanf("%d", &num1); //indica sin signo
    printf("Introduzca el segundo n�mero: ");
    scanf("%d", &num2); //indica sin signo


    if (num1 == num2)
    {
        num1=num1*num2;
        printf("multiplicacion = %d",num1);  }      
        else 
            if(num1>num2){
                num1=num1-num2;
                printf("resta = %d",num1); }
                else {
                    num1=num1+num2;
                    printf("suma = %d",num1);}
                
                  


}