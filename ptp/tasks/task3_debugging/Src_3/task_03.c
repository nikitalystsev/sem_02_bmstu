#include <stdio.h>

#define ER_DIV_BY_ZERO 1

int div(int a, int b);

int main(void)
{
    int a = 5, b = 2;
    if (b == 0)
        return ER_DIV_BY_ZERO;

    printf("%d div %d = %d\n", a, b, div(a, b));

    a = 10;
    b = 0;
    if (b == 0)
        return ER_DIV_BY_ZERO;
    printf("%d div %d = %d\n", a, b, div(a, b));

    return 0;
}

int div(int a, int b)
{
    return a / b;
}
