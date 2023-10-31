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

int unique_elements(int *ptr_start, int *ptr_end)
{
    int count_elem = 0;
    int diff = 0;
    for (int *pcur = ptr_start; pcur < ptr_end; pcur++)
    {
        for (int *pcur2 = pcur; pcur2 < ptr_end; pcur2++)
        {
            if (*pcur == *pcur2)
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

    int *ptr_start = a;
    int *ptr_end = a + n;
    
    // "Разогрев"
    memcpy(a, src, sizeof(src));
    unique_elements(ptr_start, ptr_end);

    memcpy(a, src, sizeof(src));
    
    beg = milliseconds_now();
    for (int i = 0; i < N_REPS; i++)
    {
        memcpy(a, src, sizeof(src));
        count_elem = unique_elements(ptr_start, ptr_end);
    }
    end = milliseconds_now();
    
    a[0] = a[1];
    a[1] = count_elem;

    count_elem = 1000;

    a[2] = 10000;

    count_elem = unique_elements(ptr_start, ptr_end);

    FILE *pFile;
    pFile = fopen("myfile.txt","w");
    fprintf(pFile, "count_elem %d\n", count_elem);
    fclose (pFile);

    printf("%g\n", (double) (end - beg) / N_REPS);


    return SUCCESS;
}
