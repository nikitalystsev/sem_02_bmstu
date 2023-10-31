#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <math.h>

#ifndef N
#error  where?
#endif

#define SUCCESS 0

#define EPS 1e-9

void swap(double *a, double *b)
{
    double temp = *a;
    *a = *b;
    *b = temp;
}

int selection_sort(double *a, size_t n)
{
    for (size_t i = 0; i < n - 1; i++)
    {
        double min_elem = a[i];
        size_t min_ind = i;
        for (size_t j = i + 1; j < n; j++)
            if (a[j] < min_elem)
            {
                min_elem = a[j];
                min_ind = j;
            }
        if (min_ind != i)
            swap(&a[i], &a[min_ind]);  
    }
    return SUCCESS; 
}

int main(void)
{
    double a[N];
    double elem; 
    int ind = 0;
    int number_lower_quartile;
    double lower_quartile;
    if (scanf("%lf", &elem) == 1)
        a[ind] = elem;

    ind++;
    while (scanf("%lf", &elem) == 1 && ind < N)
        a[ind++] = elem;

    selection_sort(a, ind);

    
    double n = 0.25 * (ind + 1);

    if (fabs(n - (int) n) < EPS)
    {
        number_lower_quartile = (int) n;
        lower_quartile = a[number_lower_quartile];
    }
    else
        lower_quartile = (a[(int) n] + a[(int) n + 1]) / 2;

    printf("%lf", lower_quartile);

    return SUCCESS;
}