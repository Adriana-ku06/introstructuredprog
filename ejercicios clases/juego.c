#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// juego de piedra papel y tijera contra la computadora

int juego(int x, int num){

  char *jugador;
  char *computadora; 
////////////////////////////
/*asignar valor a jugador*/

switch (x) {
    case 1:  jugador="piedra"; break;
    case 2:  jugador="papel"; break;
     case 3:  jugador="tijera"; break;
        exit(1);
  }
/////
/*asignar valor a computadora*/
switch (num) {
    case 1:  computadora="piedra"; break;
    case 2:  computadora="papel"; break;
     case 3:  computadora="tijera"; break;
        exit(1);
  }

//////////////////////
if(strcmp(jugador,"piedra")==0 && strcmp(computadora,"tijera")==0){
  printf("mi respuesta es%s\n tu respuesta es %s\n Es un empate",computadora, jugador);
      printf("Haz ganado");
    
}

if(strcmp(jugador,"tijeras")==0 && strcmp(computadora,"papel")==0){
  printf("mi respuesta es%s\n tu respuesta es %s\n ",computadora, jugador);
      printf("Haz ganado");     

}
else if(strcmp(jugador,"papel")==0 && strcmp(computadora,"piedra")==0){
  printf("mi respuesta es %s\n tu respuesta es %s\n ",computadora, jugador);
      printf("Haz ganado");     

}
    

  else if(strcmp(jugador,computadora)==0){
    printf("mi respuesta es %s\n tu respuesta es %s\n ",computadora, jugador);
      printf("Es un empate");
  }
  
            else{
            printf("mi respuesta es %s\n tu respuesta es %s\n ",computadora, jugador);
              printf("Haz perdido");

          }
        
return 0;


}


int main() {
  printf("Hola como estas jugamos piedra papel y tijeras?\n");
   printf("Introduce 1 para SI Y 2 para NO \n");
     int res, num;
     int seleccion;
    scanf("%d", &res);

    if(res==1){
        printf("Juguemos :D\n");
            printf("PIEDRA, PAPEL O TIJERA \n");
             printf("Introduce 1 ===>PIEDRA \n");
             printf("Introduce 2 ===>PAPEL \n");
             printf("Introduce 3 ===>TIJERA \n");            
            scanf("%d", &seleccion);
               num= rand()%3;//asignar valor a computadora
            juego(seleccion, num);






    }
    else {
printf("Juguemos en otro momento, BYE!, :D");

    }

   
  return 0;
}