#include <stdio.h>

int main(void)
{
    char c;
    short h;
    char *p;
    int i;

    printf("c %p (%zu, %p)\n", (void*) &c, sizeof(c), (char*) &c + sizeof(c));
    printf("h %p (%zu, %p)\n", (void*) &h, sizeof(h), (char*) &h + sizeof(h));
    printf("p %p (%zu, %p)\n", (void*) &p, sizeof(p), (char*) &p + sizeof(p));
    printf("i %p (%zu, %p)\n", (void*) &i, sizeof(i), (char*) &i + sizeof(i));

    return 0;
}
