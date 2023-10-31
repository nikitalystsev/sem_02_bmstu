/*
Слайд 18
*/

#include <stdio.h>

struct s
{
   int a[5];
};

void f(struct s elem)
{
   for (int i = 0; i < 5; i++)
      elem.a[i] = 0;
}

int main(void)
{
    struct s s_1 = {{1, 2, 3, 4, 5}};
    struct s s_2;

    s_2 = s_1;

    for(int i = 0; i < 5; i++)
        printf("%d ", s_2.a[i]);

    printf("\n");

    f(s_2);

    for(int i = 0; i < 5; i++)
        printf("%d ", s_2.a[i]);

    return 0;
}