/*
Write a program to input any character and check whether it is alphabet, digit or
special character.
*/

#include <stdio.h>
#include <ctype.h>
int main(void) 
{
  char caracter;
  printf("Escribe un carácter:\n");
  scanf("%c", &caracter);
  if (isalpha(caracter)) {// isalpha permite saber si es una letra 
    printf("Es una letra del Abecedario");
  } 
  
  else {
    
    if(isdigit(caracter)){// isdigit permite saber si es un numero 
      printf("Es  un numero");
    }
    else{
    printf("Es un caracter especial");}
  }
  return 0;
}

