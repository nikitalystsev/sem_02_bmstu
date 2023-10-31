/*
Cлайд 9
*/

#include <stdio.h>

int main(void)
{
    struct s_1
    {
        char a;
        int b;
    } c1;

    printf("&c1 %p, &c1.a %p\n", (void*) &c1, (void*) &c1.a);
    printf("sizeof(c1) = %d\n", sizeof(c1));

    return 0;
}