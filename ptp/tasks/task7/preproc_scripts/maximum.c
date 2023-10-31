#include <stdio.h>
#include <limits.h>

#define SUCCESS 0

int main(void)
{
    double max;
    double elem;

    if (scanf("%lf", &elem) == 1)
        max = elem;

    while (scanf("%lf", &elem) == 1)
        if (elem > max)
            max = elem;

    printf("%lf", max);

    return SUCCESS;
}