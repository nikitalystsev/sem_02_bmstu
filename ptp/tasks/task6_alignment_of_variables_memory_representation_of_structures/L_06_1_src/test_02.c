/*
Слайд 4
*/

#include <stdio.h>
#include "test_02.h"

void print_today(void)
{
    struct date today;

    (void) today;
}

int main(void)
{
    struct date some_date;

    (void) some_date;

    /*	
    error: unknown type name 'date'; use 'struct' keyword to refer to the type	
	date another_date;
    */
    
    print_today();

    return 0;
}
