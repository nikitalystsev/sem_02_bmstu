/*
Слайд 24
*/

#include <assert.h>
#include <stdio.h>

typedef enum { KIND_INT, KIND_DOUBLE } kind_num_t;

typedef struct
{
    kind_num_t kind;

    union
    {
        int i;
        double d;
    } u;

} number_t;

void print_number(const number_t *num)
{
    if (num->kind == KIND_INT)
    {
        printf("%d\n", num->u.i);
    } 
    else if (num->kind == KIND_DOUBLE)
    {
        printf("%g\n", num->u.d);
    }
    else
    {
        assert(0);
    }
}

int main(void)
{
    number_t arr[10];

    arr[0].kind = KIND_INT;
    arr[0].u.i = 10;

    arr[1].kind = KIND_DOUBLE;
    arr[1].u.d = 7.555;

    print_number(arr);

    print_number(arr + 1);

    return 0;
}
