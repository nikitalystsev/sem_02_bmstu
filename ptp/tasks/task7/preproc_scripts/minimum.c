#include <stdio.h>
#include <limits.h>

#define SUCCESS 0

int main(void)
{
    double min;
    double elem;

    if (scanf("%lf", &elem) == 1)
        min = elem;

    while (scanf("%lf", &elem) == 1)
        if (elem < min)
            min = elem;

    printf("%lf", min);

    return SUCCESS;
}