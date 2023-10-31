/*
Cлайды 23, 24
*/

#include <stdio.h>

int main(void)
{
    struct
    {
        int i;
        double d;
    } s;

    union
    {
        int i;
        double d;
    } u;

    printf("sizeof(s) %d\n", sizeof(s));
    printf("&s %p, &s.i %p, &s.d %p\n", (void*) &s, (void*) &s.i, (void*) &s.d);
    printf("sizeof(u) %d\n", sizeof(u));
    printf("&u %p, &u.i %p, &u.d %p\n", (void*) &u, (void*) &u.i, (void*) &u.d);

    printf("u.i %d, u.d %g\n", u.i, u.d);

    u.i = 5;

    printf("u.i %d, u.d %g\n", u.i, u.d);

    u.d = 5.25;

    printf("u.i %d, u.d %g\n", u.i, u.d);

    return 0;
}