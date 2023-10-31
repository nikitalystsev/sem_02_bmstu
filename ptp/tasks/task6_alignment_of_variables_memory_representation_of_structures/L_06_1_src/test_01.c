/*
Слайд 4
*/

#include <stdio.h>

void print_today(void)
{
    struct date
    {
        int day;
        int month;
        int year;

    } today;

    (void) today;
}

int main(void)
{
    /*
    error: storage size of 'some_date' isn't known
    struct date some_date;
    */
    
    print_today();

    return 0;
}
