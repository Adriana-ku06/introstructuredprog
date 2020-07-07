Reference :
https://fresh2refresh.com/c-programming/c-array/
http://www.btechsmartclass.com/c_programming/C-Types-of-Arrays.html
http://www.c4learn.com/c-programming/c-array-types/

# Types of Arrays in C
In c programming language, arrays are classified into two types. They are as follows:
*	One dimensional array
*	Multi dimensional array

## Single Dimensional Array
In c programming language, single dimensional arrays are used to store list of values of same datatype. In other words, single dimensional arrays are used to store a row of values. In single dimensional array, data is stored in linear form. Single dimensional arrays are also called as one-dimensional arrays, Linear Arrays or simply 1-D Arrays.
Declaration of Single Dimensional Array:
Example:
``` C
int rollNumbers [60];
char list [6];
int numbers[50]
``` 


### Initialization of Single Dimensional Array
We use the following general syntax for declaring and initializing a single dimensional array with size and initial values.

Example:

``` C
int list [6] = { 9, 0, 6, 8, 8, 8 };
```

## Multi Dimensional Array
An array of arrays is called as multi dimensional array. In simple words, an array created with more than one dimension (size) is called as multi dimensional array. Multi dimensional array can be of two dimensional array or three dimensional array or four dimensional array or more...

Most popular and commonly used multi dimensional array is two dimensional array. The 2-D arrays are used to store data in the form of table. We also use 2-D arrays to create mathematical matrices.

Example:
``` C
int matrix_A [2][3];
```
### Initialization of Two Dimensional Array

We use the following general syntax for declaring and initializing a two dimensional array with specific number of rows and coloumns with initial values.

Example:
``` C
int matrix_A [2][3] = { {1, 2, 3},{4, 5, 6} } ;
```
