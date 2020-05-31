Adriana Ku Huchim :https://github.com/Adriana-ku06/programming2
# Subprograms
A subprogram is a program unit that can be invoked from another program unit to perform a specific task. These subprograms are either written by the user or supplied as part of the Fortran library.



* Statement functions: A computing procedure defined by a single statement that is similar in form to an assignment statement. A statement function is invoked by a function reference in a main program unit or a subprogram unit.
Function subprograms: Program units, also called functions, that contain a set of commonly used computations. A function subprogram's first statement is a FUNCTION statement, optionally preceded by an OPTIONS statement. A function subprogram is invoked by a function reference in a main program unit or a subprogram unit.
* Subroutine subprograms: Program units, also called subroutines, that contain a set of commonly used computations. A subroutine subprogram's first statement is a SUBROUTINE statement, optionally preceded by an OPTIONS statement. A subroutine subprogram receives control when it is invoked with a CALL statement and returns control with a RETURN statement.
* Subprograms supplied as part of the Fortran library are called intrinsic subprograms (or procedures). They perform mathematical, numeric, bit manipulation, character, and miscellaneous functions.

## By Value
The call by value method of passing arguments to a subprogram copies the actual value of an argument into the formal parameter of the subprogram. In this case, changes made to the parameter inside the function have no effect on the argument.

By default, Pascal uses call by value method to pass arguments. In general, this means that code within a subprogram cannot alter the arguments used to call the subprogram.
```C
#include <stdio.h>
char toUpperByValue(char);
int main()
{
 char letra = 'a';
 printf("El valor inicial de la variable letra es %c\n", letra);
 letra = toUpperByValue(letra);
 printf("El nuevo valor de la variable letra es %c\n", letra);
 return 0;
}
char toUpperByValue(char c)
{
 if (c >= 'a' && c < 'z') /* es una letra minuscula */
 c = c - 32; /* la cambia a mayúscula */
 return c;
} 

```

   

## By Reference
Passing by reference is the term that generates the most controversy in the world of computing; therefore, if we want to properly use this statement, the word must be defined first: reference.

A reference is, in a broad sense, a value that allows us to indirectly access a particular datum within a program; This data could be found, for example, in the main memory of a computer. Putting it in simpler words, if something refers to a data, that something is considered a reference.

References take different forms and may be known differently in one programming language or another. Knowing how to identify references will become a very important skill that will allow us to make correct use of them (and by the way save us a few hours of debugging). There is no way to get lost, you just have to always keep in mind the main idea that we have already discussed. Let's move on to see some reference implementations.
``` C
#include <stdio.h>
void toUpperByReference(char *);
int main()
{
 char letra = 'a'; 
printf("El valor inicial de la variable letra es %c\n", letra);
 toUpperByReference(&letra);
 printf("El nuevo valor de la variable letra es %c\n", letra);
 return 0;
} 


```

# Recursion
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function. Using recursive algorithm, certain problems can be solved quite easily. Examples of such problems are Towers of Hanoi (TOH), Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.
In the recursive program, the solution to the base case is provided and the solution of the bigger problem is expressed in terms of smaller problems.
```  
int fact(int n)
{
    if (n < = 1) // base case
        return 1;
    else    
        return n*fact(n-1);    
} 

```

## Direct
A function is called direct recursive if it calls the same function . 
```
// An example of direct recursion
void directRecFun()
{
    // Some code....

    directRecFun();

    // Some code...
}

```
## Indirect
There is also indirect recursion, where several functions depend upon one another

Occurs when a function is called not by itself but by another function that it called (either directly or indirectly). For example, if f calls f, that is direct recursion, but if f calls g which calls f, then that is indirect recursion of f.
```
void indirectRecFun2()
{
    // Some code...

    indirectRecFun1();

    // Some code...
}
```


# References
* C: [Funciones. Pasaje de parámetros por valor y por referencia](http://programacionnerd.blogspot.com/2012/05/c-funciones-pasaje-de-parametros-por.html)
* [Direct vs. Indirect Recursion](https://www.educative.io/courses/recursion-for-coding-interviews-in-cpp/BnKojpzLl2W)
* [Recursion in C Programming](https://www.programtopia.net/c-programming/docs/recursion-c-programming)
* [Subprogram](https://www.fing.edu.uy/inco/cursos/prog1/pm/uploads/Materiales/clase8.html#id283705) 
