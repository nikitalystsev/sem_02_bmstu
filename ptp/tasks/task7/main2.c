// c99
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <sys/time.h>

#ifndef NMAX 
#error  where?
#endif
#define N_REPS    1

#define ERR_WRONG_INPUT 1
#define ERR_WRONG_DIMENSION 2
#define ERR_EXPR_NO_CALC 3
#define SUCCESS 0

// Получение времени в миллисекундах
unsigned long long milliseconds_now(void)
{
    struct timeval val;

    if (gettimeofday(&val, NULL))
        return (unsigned long long) -1;

    return val.tv_sec * 1000ULL + val.tv_usec / 1000ULL;
}

int unique_elements(int *array, size_t size)
{
    int count_elem = 0;
    int diff = 0;
    for (size_t i = 0; i < size; i++)
    {
        for (size_t j = i; j < size; j++)
        {
            if (*(array + i) == *(array + j))
                count_elem++;
            if (count_elem > 1) 
                break;
        }
        if (count_elem == 1)
            diff++;
        count_elem = 0;
    }

    return diff;
}

int main(void)
{
    int a[NMAX], src[NMAX];
    size_t n = sizeof(a) / sizeof(a[0]);
    long long unsigned beg, end;
    int count_elem;

    srand(time(NULL));
    
    for (size_t i = 0; i < n; i++)
        src[i] = rand();
    
    // "Разогрев"
    memcpy(a, src, sizeof(src));
    unique_elements(a, n);

    memcpy(a, src, sizeof(src));

    beg = milliseconds_now();

    for (int i = 0; i < N_REPS; i++)
    {
        memcpy(a, src, sizeof(src));
        count_elem = unique_elements(a, n);
    }

    end = milliseconds_now();

    a[0] = a[1];
    a[1] = count_elem;

    count_elem = 1000;

    a[2] = 10000;

    count_elem = unique_elements(a, n);

    FILE *pFile;
    pFile = fopen("myfile.txt","w");
    fprintf(pFile, "count_elem %d\n", count_elem);
    fclose (pFile);

    printf("%g\n", (double) (end - beg) / N_REPS);

    return SUCCESS;
}
