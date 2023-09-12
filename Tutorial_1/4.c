/* Prints the larger of two integers*/
#include <stdio.h>
#include <stdlib.h>

int larger (int, int );

int larger (int a, int b) {
/* Returns the larger of two ints passed as arguments */
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int main () {
    int inA, inB, result, choice;
    inA = 5;
    inB = 6;
    result = larger (inA, inB) ;
    printf ("The larger of %d and %d" , inA , inB);
    printf (" is %d" , result);
    scanf ("%d", &choice);
    return 0;
}