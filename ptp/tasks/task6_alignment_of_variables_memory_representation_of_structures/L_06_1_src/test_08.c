/*
Cлайд 17
*/

#include <stdio.h>


struct date
{
    int day;
    int month;
    int year;
};

void print(struct date d)
{
    printf("%02d.%02d.%04d\n", d.day, d.month, d.year);
}

void print_ex(const struct date *d)
{
    printf("%02d.%02d.%04d\n", d->day, d->month, d->year);
}

struct date get_student_date(void)
{
    struct date d = {25, 1, 2021};

    return d;
}

int main(void)
{
    struct date today, some_date;

    today.day   = 19;
    today.month = 4;
    today.year  = 2022;

    some_date = today;

    print(today);

    print_ex(&some_date);

    some_date = get_student_date();

    print_ex(&some_date);

    return 0;
}