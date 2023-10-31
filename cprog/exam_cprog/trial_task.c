#include <stdio.h>
#include <stdlib.h>

#define N 5
#define M 7

#define SIZE 35

#define ERR_WRONG_INPUT 1
#define ERR_WRONG_DIMENSION 2
#define SUCCESS 0

void print_array(const unsigned short int *const array, size_t m)
{
    for (size_t i = 0; i < m; i++)
        printf("%d ", array[i]);
}

void print_matrix(unsigned short int matrix[][M], size_t n, size_t m)
{
    for (size_t i = 0; i < n; i++)
    {
        print_array(matrix[i], m);
        printf("\n");
    }
}

int get_dimensions(size_t *const n, size_t *const m)
{
    int rc = scanf("%lu %lu", n, m); 
    if (rc != 2)
    {
        printf("Input error");
        return ERR_WRONG_INPUT; 
    }
    if (*n <= 0 || *n > N)
    {
        printf("Range error");
        return ERR_WRONG_DIMENSION;
    }
    if (*m <= 0 || *m > M)
    {
        printf("Range error");
        return ERR_WRONG_DIMENSION;
    }

    return SUCCESS;
}

int matrix_init(unsigned short int matrix[][M], size_t n, size_t m)
{
    for (size_t i = 0; i < n; i++)
        for (size_t j = 0; j < m; j++) 
        {
            unsigned short int numb;
            int rc = scanf("%hu", &numb);
            if (rc != 1)
            {
                printf("Unknown error");
                return ERR_WRONG_INPUT;
            }
            matrix[i][j] = numb;
        }

    return SUCCESS;
}

void init_array(unsigned short int array[], 
size_t *const n_array, unsigned short int matrix[][M],
size_t n, size_t m)
{
    for (size_t i = 0; i < n; i++)
        for (size_t j = 0; j < m; j++) 
        {
            if ((matrix[i][j] & (1 << 3)) || (matrix[i][j] & (1 << 4)))
            {
                array[*n_array] = matrix[i][j];
                (*n_array)++;           
            }
        }
}

int main(void)
{
    size_t n = 0, m = 0, n_array = 0;

    unsigned short int matrix[N][M];
    unsigned short int array[SIZE];

    int rc = get_dimensions(&n, &m);
    if (rc != 0)
        return rc;
    rc = matrix_init(matrix, n, m);
    if (rc != 0)
        return rc;
    init_array(array, &n_array, matrix, n, m);
    if (n_array != 0)
        print_array(array, n_array);
    else
        printf("Empty array");

    return SUCCESS;
}