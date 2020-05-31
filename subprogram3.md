# Subprograms
A subprogram is a program unit that can be invoked from another program unit to perform a specific task. These subprograms are either written by the user or supplied as part of the Fortran library.



* Statement functions: A computing procedure defined by a single statement that is similar in form to an assignment statement. A statement function is invoked by a function reference in a main program unit or a subprogram unit.
Function subprograms: Program units, also called functions, that contain a set of commonly used computations. A function subprogram's first statement is a FUNCTION statement, optionally preceded by an OPTIONS statement. A function subprogram is invoked by a function reference in a main program unit or a subprogram unit.
* Subroutine subprograms: Program units, also called subroutines, that contain a set of commonly used computations. A subroutine subprogram's first statement is a SUBROUTINE statement, optionally preceded by an OPTIONS statement. A subroutine subprogram receives control when it is invoked with a CALL statement and returns control with a RETURN statement.
* Subprograms supplied as part of the Fortran library are called intrinsic subprograms (or procedures). They perform mathematical, numeric, bit manipulation, character, and miscellaneous functions.

## By Value
The call by value method of passing arguments to a subprogram copies the actual value of an argument into the formal parameter of the subprogram. In this case, changes made to the parameter inside the function have no effect on the argument.

By default, Pascal uses call by value method to pass arguments. In general, this means that code within a subprogram cannot alter the arguments used to call the subprogram.

   ![Figure 1-1](http://2.bp.blogspot.com/-F6YWx-olIXA/T7RYUUp_WiI/AAAAAAAAAgQ/4lr7rSTolo4/s1600/pasoporvalor2.png)

## By Reference
Passing by reference is the term that generates the most controversy in the world of computing; therefore, if we want to properly use this statement, the word must be defined first: reference.

A reference is, in a broad sense, a value that allows us to indirectly access a particular datum within a program; This data could be found, for example, in the main memory of a computer. Putting it in simpler words, if something refers to a data, that something is considered a reference.

Based on the above, how would you define a step by reference now? Very simple, if you give a function a reference, this form of variable pass is, in all rule, one step per reference. Still, it is worth mentioning that the designers of programming languages will not make it so easy for us and will manage, perhaps without being their true intention, to complicate our lives.

References take different forms and may be known differently in one programming language or another. Knowing how to identify references will become a very important skill that will allow us to make correct use of them (and by the way save us a few hours of debugging). There is no way to get lost, you just have to always keep in mind the main idea that we have already discussed. Let's move on to see some reference implementations.

![Figure 1-2](http://3.bp.blogspot.com/-Dqvq0L71nNI/T7RcbODb47I/AAAAAAAAAg8/RDZ6lB8eU8o/s1600/pasoporreferencia2.png)

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
A function fun is called direct recursive if it calls the same function fun. A function fun is called indirect recursive if it calls another function say fun_new and fun_new calls fun directly or indirectly. 
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
There is also indirect recursion, where several functions depend upon one another. For instance, function A calls function B, which calls function C. If function C, under any circumstances, calls back to function A, this is a case of indirect recursion.

Occurs when a function is called not by itself but by another function that it called (either directly or indirectly). For example, if f calls f, that is direct recursion, but if f calls g which calls f, then that is indirect recursion of f.
```
void indirectRecFun2()
{
    // Some code...

    indirectRecFun1();

    // Some code...
}
```
