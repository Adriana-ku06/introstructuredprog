#include <stdio.h>
#include <stdlib.h>

typedef struct razon * fraccion;

int EuclidesMCD(int a, int b);
int EuclidesMCM(int a, int b);
fraccion nueva(int n, int d);
void imprime(fraccion a);
fraccion suma(fraccion a, fraccion b);
fraccion resta(fraccion a, fraccion b);

struct razon {
   int numerador;
   int denominador;
};

int EuclidesMCD(int a, int b){

    int aux;
    int mayor = a > b ? a : b;
    int menor = a < b ? a : b;
    
    do{
        aux = menor;
        menor = mayor % menor;
        mayor = aux;  
    } while(menor!=0);
    return mayor;
}

int EuclidesMCM(int a, int b) {
    return(a/EuclidesMCD(a,b))*b;
}

fraccion nueva(int n, int d) {
    fraccion aux;
    int mcd, signo;
    
    aux = (fraccion) malloc(sizeof(struct razon));
    
    signo = (float)n/(float)d > 0 ? 1 : -1;
    
    d = d>0 ? d: -d;
    n = n>0 ? n: -n;
    
    mcd = EuclidesMCD(n, d);
    
    aux->numerador = signo*n/mcd;
    aux->denominador = d/mcd;
    
            
    return aux;    
}

void imprime(fraccion a) {
   printf("%d/%d \n", a->numerador, a->denominador);
}

fraccion suma(fraccion a, fraccion b) {
   fraccion aux;

   int num, den;
   den = a->denominador * b->denominador;
   num = a->numerador * b->denominador + a->denominador * b->numerador;

   aux = nueva(num, den);
   
   return aux;
}

fraccion resta(fraccion a, fraccion b) {
   fraccion aux;

   int num, den;
   den = a->denominador * b->denominador;
   num = a->numerador * b->denominador - a->denominador * b->numerador;

   aux = nueva(num, den);
   
   return aux;
}

fraccion multiplicacion(fraccion a, fraccion b){

   return nueva(a->numerador*b->numerador,  a->denominador*b->denominador);
}

fraccion division(fraccion a, fraccion b){

   return nueva(a->numerador*b->denominador,  a->denominador*b->numerador);
}

int main(){
   fraccion a = nueva(20, -30);
   fraccion b = nueva(4, 20);
   fraccion c;

   imprime(a);
   imprime(b);
   c = suma(a, b);
   imprime(c);
   c = resta(a, b);
   imprime(c);
   c = multiplicacion(a, b);
   imprime(c);
   c = division(a, b);
   imprime(c);
}