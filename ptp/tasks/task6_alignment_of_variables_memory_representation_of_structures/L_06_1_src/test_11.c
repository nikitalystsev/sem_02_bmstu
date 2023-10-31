/*
Cлайд 21
*/

#include <stdio.h>

int main(void)
{
    union u_t
    {
        int i;
        double d;
    };
	
    union u_t  u_1 = {1};

    // только c99
    union u_t  u_2 = { .d = 5.25 };

    (void) u_1;
    (void) u_2;

    return 0;
}