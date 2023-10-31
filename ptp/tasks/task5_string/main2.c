#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SIZE 4

int main(void)
{
    char arr_1[][6] = {"One", "Two", "Three", "Four"};
    const char *arr_2[] = {"one", "two", "three", "four"};
    for (size_t i = 0; i < SIZE; i++)
    {
        printf("%s \n", arr_1[i]);
	printf("%s \n", arr_2[i]);
    }
    
    return EXIT_SUCCESS;
}
