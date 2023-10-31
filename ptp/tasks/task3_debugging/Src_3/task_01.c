#include <stdio.h>

long long unsigned factorial(unsigned n);

int main(void)
{
    unsigned n;
    long long unsigned result;

    printf("Input n: ");
    if (scanf("%u", &n) != 1)
    {
        printf("Input error");
        return 1;
    }

    result = factorial(n);

    printf("factorial(%u) = %llu\n", n, result);

    return 0;
}

long long unsigned factorial(unsigned n)
{
    long long unsigned result = 1;

    while (n)
    {
        result *= n;
        n--;
    }
    return result;
}
