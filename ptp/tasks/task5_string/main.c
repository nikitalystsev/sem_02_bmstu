#include <stdio.h>
#include <string.h>

int main(void)
{
    const char *s1 = "Hello world";
    const char s2[] = "Hello world";
    const char s3[20] = "Hello world";

    const char s4[20] = {'H', 'e', 'l', 'l', 'o', '\0'};

    const char a[][11] = {"name", "surname", "patronymic"};
    const char *a2[] = {"name", "surname", "patronymic"};

    printf("%s   %s   %s   %s\n", s1, s2, s3, s4);
    printf("%s\n", a[0]);
    printf("%s\n", a2[0]);

    return 0;
}