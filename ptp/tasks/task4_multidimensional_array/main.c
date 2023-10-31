#include <stdio.h>
int processing_elem_array(int elem_array);

int main(void)
{
    int a[2][3][4] =
    {
        {
            {1, 2, 3, 4},
            {5, 6, 7 ,8},
            {9, 10, 11, 12}
        },
        {
            {12, 11, 10, 9},
            {8, 7, 6, 5},
            {4, 3, 2, 1}
        }
    };
    int (*p)[3][4] = a;
    int (*q)[4] = a[0];
    int *r = a[0][0];
    int s = a[0][0][0];
    printf("p = %p  p + 1 = %p\n", (void *) p, (void *) (p + 1));
    printf("a = %p a + 1 = %p\n", (void *) a, (void *) (a + 1));
    printf("\n");
    printf("q = %p  q + 1 = %p\n", (void *) q, (void *) (q + 1));
    printf("a[0] = %p  a[0] + 1 = %p\n", (void *) a[0], (void *) (a[0] + 1));

    printf("r = %p  r + 1 = %p\n", (void *) r, (void *) (r + 1));
    printf("a[0][0] = %p  a[0][0] + 1 = %p\n", (void *) a[0][0], (void *) (a[0][0] + 1));
    printf("%d\n", s);
    return 0;
}
