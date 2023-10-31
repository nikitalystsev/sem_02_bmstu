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

    #pragma pack(push, 1)
    struct s_2
    {
        char a;
        int b;
    } c2;
    #pragma pack(pop)

    printf("sizeof(c1) = %d\n", sizeof(c1));
    printf("&c1 %p, &c1.a %p\n", (void*) &c1, (void*) &c1.a);

    printf("sizeof(c2) = %d\n", sizeof(c2));
    printf("&c2 %p, &c2.a %p\n", (void*) &c2, (void*) &c2.a);

    return 0;
}