#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_SIZE    10

int main(void)
{
    int matrix[MAX_SIZE][MAX_SIZE];
    int size;
    scanf("%d", &size);

    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            if (scanf("%d", &matrix[i][j]) != 1)
                return EXIT_FAILURE;

    int min = INT_MIN;

    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            if (i < j && matrix[i][j] % 2 == 1 && matrix[i][j] > min)
                min = matrix[i][j];

    printf("%d\n", min);

    return EXIT_SUCCESS;
}               
