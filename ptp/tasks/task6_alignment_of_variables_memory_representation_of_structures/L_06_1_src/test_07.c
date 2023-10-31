/*
Cлайды 15-16
*/

#include <stdio.h>

struct date
{
    int day;
    int month;
    int year;
};

int main(void)
{
    struct date today, *some_date = &today;

    today.day   = 19;
    today.month = 4;
    today.year  = 2022;

    (*some_date).day   = 1;
    (*some_date).month = 6;
    (*some_date).year  = 2022;

    printf("%02d.%02d.%4d\n", some_date->day, some_date->month, some_date->year);

    /*
    error: invalid operands to binary == (have 'struct date' and 'struct date')     
    if (today == *some_date)
    {
        ;
    }
    */

    return 0;
}