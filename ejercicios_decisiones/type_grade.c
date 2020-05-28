/*
Write a C program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.

Calculate percentage and grade according to following:

Percentage >= 90% : Grade A

Percentage >= 80% : Grade B

Percentage >= 70% : Grade C

Percentage >= 60% : Grade D

Percentage >= 40% : Grade E

Percentage < 40% : Grade F

entrada ejemplo
orden
 (Physics, Chemistry, Biology, Mathematics and Computer)
 entrada
./a.aout 70 80 90 50 60

*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[])
        {
        int i = 0;
            int calf;
             char *mat;
             //printf("%d", argc);
      
       
        for(i=1; i<argc; i++) {
            if(i==1){
                //Physics  , Chemistry, Biology, Mathematics and Computer
                mat="Physics";     
                }
                if(i==2){
                 mat="Chemistry";     
                }
                 if(i==3){
                 mat="Biology";     
                }
                 if(i==4){
                 mat="Mathematics";     
                }
                 if(i==5){
                 mat="Computer";     
}                }

            printf("Materia %s %s\n",mat,argv[i]);
                if(atoi(argv[i])>=90 && atoi(argv[i])<=100){
                printf("%s is GRADE A \n",mat);     
                }
                else{
                    if(atoi(argv[i])>=80 && atoi(argv[i])<90){printf("%s is GRADE B \n",mat); }
                    else{
                       if(atoi(argv[i])>=70 && atoi(argv[i])<80){printf("%s is GRADE C \n",mat); }
                       else{
                             if(atoi(argv[i])>=60 && atoi(argv[i])<70){printf("%s is GRADE D \n",mat); }
                             else{
                               if(atoi(argv[i])>=40 && atoi(argv[i])<60){printf("%s is GRADE E \n",mat); }
                                  else{
                                    if(atoi(argv[i])<40){printf("%s is GRADE F\n",mat); }
                             }
                             


                             }

                       }


                    }

                  
               

                }

            
        }
       
      
        
return 0;
