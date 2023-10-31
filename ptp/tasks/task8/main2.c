// c99
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

#ifndef NMAX 
#error  where?
#endif

// Получение времени в миллисекундах
unsigned long long milliseconds_now(void)
{
    struct timeval val;

    if (gettimeofday(&val, NULL))
        return (unsigned long long) -1;

    return val.tv_sec * 1000ULL + val.tv_usec / 1000ULL;
}

void calc_sums_row(int (*const matrix)[NMAX], int *const sum_rows)
{
    for (size_t i = 0; i < NMAX; i++)
    {
        int sum = 0;
        for (size_t j = 0; j < NMAX; j++)
            sum += matrix[i][j];
        sum_rows[i] = sum;
    }
}

void swap(int *const array1, int *const array2)
{
    for (size_t i = 0; i < NMAX; i++)
    {
        int tmp = array1[i];
        array1[i] = array2[i];
        array2[i] = tmp;
    }
}

int bubble_sort(int (*const matrix)[NMAX], int *const sum_rows)
{
    for (size_t i = 0; i < NMAX - 1; i++)
        for (size_t j = 0; j < NMAX - 1 - i; j++)
        {
            if (sum_rows[j] > sum_rows[j + 1])
            {
                swap(matrix[j], matrix[j + 1]);

                int tmp = sum_rows[j];
                sum_rows[j] = sum_rows[j + 1];
                sum_rows[j + 1] = tmp;
            }
        }
    return EXIT_SUCCESS; 
}

void init_matrix(int (*const matrix)[NMAX])
{
    srand(time(NULL));
    
    for (size_t i = 0; i < NMAX; i++)
        for (size_t j = 0; j < NMAX; j++)
            matrix[i][j] = rand();
}

int main(void)
{
    int a[NMAX][NMAX];
    int sum_rows[NMAX];
    long long unsigned beg, end;
    int count_elem;

    init_matrix(a);


    beg = milliseconds_now();

    calc_sums_row(a, sum_rows);
    count_elem = bubble_sort(a, sum_rows);

    end = milliseconds_now();


    a[0][0] = a[0][1];
    a[0][1] = a[1][1];

    a[0][2] = a[2][1];
    a[0][0] = a[0][1];

    a[3][0] = a[2][1];
    a[0][2] = a[3][1];

    count_elem = bubble_sort(a, sum_rows);

    FILE *pFile;
    pFile = fopen("myfile.txt","w");
    fprintf(pFile, "count_elem %d\n", count_elem);
    fclose (pFile);

    printf("%g\n", (double) (end - beg));

    return EXIT_SUCCESS;
}