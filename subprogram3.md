# Subprograms
A subprogram is a program unit that can be invoked from another program unit to perform a specific task. These subprograms are either written by the user or supplied as part of the Fortran library.



* Statement functions: A computing procedure defined by a single statement that is similar in form to an assignment statement. A statement function is invoked by a function reference in a main program unit or a subprogram unit.
Function subprograms: Program units, also called functions, that contain a set of commonly used computations. A function subprogram's first statement is a FUNCTION statement, optionally preceded by an OPTIONS statement. A function subprogram is invoked by a function reference in a main program unit or a subprogram unit.
* Subroutine subprograms: Program units, also called subroutines, that contain a set of commonly used computations. A subroutine subprogram's first statement is a SUBROUTINE statement, optionally preceded by an OPTIONS statement. A subroutine subprogram receives control when it is invoked with a CALL statement and returns control with a RETURN statement.
* Subprograms supplied as part of the Fortran library are called intrinsic subprograms (or procedures). They perform mathematical, numeric, bit manipulation, character, and miscellaneous functions.

## By Value

 Are the parameters not preceded by var

At the time of invocation, a copy of the values of the effective parameters to the nominal parameters is made.

The effective parameters can be expressions

Example Let the head function f (a, b: integer): boolean

The invocation: f (23, N * 2) is equivalent to the following:
    ```
    a:= 23;
    b:= N*2;  
       ``` 
    

## By Reference
They are the parameters preceded by var

The effective parameters must be variable.

At the time of invocation, the nominal parameter shares the same memory space as the effective parameter. (alias of variables).

Any changes to the nominal parameter are reflected in the effective parameter.

On the other hand, when the passage is by value, the effective parameter is not modified.

We do not recommend using passage by reference for functions.


# Recursion
## Direct
## Indirect
