/*
‘лайды 12 - 13
*/

struct date
{
    int day;
    int month;
    int year;
};

#define NAME_LEN 15

struct person
{
    char name[NAME_LEN+1];
    struct date birth;
};


int main(void)
{
    struct date today = {19, 4, 2022};

    struct date day = {19};

    /*
    struct date year = {, , 2022};
    // error: expected expression before ',' token
    */

    struct person rector = {"Aleksandrov", {7, 4, 1951}};

    struct date holidays[] = {{8, 5, 2022}, {9, 5, 2022}, {10, 5, 2022}};

    struct date year = {.year = 2022};

    struct date yesterday = {.year = 2022, .month = 4, .day = 18};

    (void) today;
    (void) day;
    (void) rector;
    (void) holidays;
    (void) year;
    (void) yesterday;
}