#include <stdio.h>

#pragma pack(push, 1)
struct s_1
{
    double b;
    int a;
    char c;
};
#pragma pack(pop)

int main(void)
{
    struct s_1 a;

    // struct s_1 f[3] = {{5, 100, 8}, {10, 200, 14}, {34, 500, 12}};

    printf("sizeof(struct s_1) = %lu\n", sizeof(struct s_1));
    printf("sizeof(a) = %lu\n", sizeof(a));
    printf("sizeof(struct f) = %lu\n", sizeof(f));
    
    a.c = '5';
    a.a = 40;
    a.b = 100;
    
    printf("sizeof(a) = %lu\n", sizeof(a));

    return 0;
}