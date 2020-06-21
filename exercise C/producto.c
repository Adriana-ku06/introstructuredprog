/*
Realizar un progrma que te permita guardar los valores de un producto, 
la informacion a guardad  del producto deben incluir codigo, descripcion y precio.

*/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct producto {
    int codigo;
    char descripcion[41];
    float precio;
};


int main()
{
    struct producto *prod;
    
    prod=malloc(sizeof(struct producto));// recervamos memoria para la variable producto
    
    prod->codigo=111;
    strcpy(prod->descripcion,"Galleta Gamesa, de 350 g ");
    prod->precio=7.50;
    
    printf("Codigo del articulo:%i\n",prod->codigo);
    printf("Descripcion:%s\n",prod->descripcion);
    printf("Precio:%0.2f",prod->precio);
    free(prod); //liberamos memoria
    
    
    return 0;
}