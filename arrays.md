Reference :
https://fresh2refresh.com/c-programming/c-array/
http://www.btechsmartclass.com/c_programming/C-Types-of-Arrays.html
http://www.c4learn.com/c-programming/c-array-types/

# Types of Arrays in C
In c programming language, arrays are classified into two types. They are as follows:
*	One dimensional array
*	Multi dimensional array

## Single Dimensional Array
In the programming language c, one-dimensional arrays are used to store a list of values of the same data type, these can be of type integer string or string.
One-dimensional arrays are used to use one row of values.
In a one-dimensional matrix, the data is stored linearly. One-dimensional matrices are also called one-dimensional matrices, linear matrices, or simply 1-D matrices.
One-dimensional array declaration:
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
An array is called as a multidimensional array when it has more than two dimensions.
  In simple words, an array created with more than one dimension (size) is called a multidimensional array.
The multidimensional matrix can be two-dimensional or three-dimensional or four or more.

Most popular and commonly used multi dimensional array is two dimensional array. 
The 2-D arrays are used to store data in the form of table. We also use 2-D arrays to create mathematical matrices.

Example:
``` C
int matrix_A [2][3];
```
### Initialization of Two Dimensional Array

The following general syntax for declaring and initializing a two-dimensional array with a specified number of rows and columns with initial values.

Example:
``` C
int matrix_A [2][3] = { {1, 2, 3},{4, 5, 6} } ;
```
