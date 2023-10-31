#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SIZE 256

void remove_extra_spaces(char *const string, char *const new_string)
{
    int j = 0;
    for (size_t i = 0; i < strlen(string); i++) 
    {
        if (string[i] == ' ') 
        {
            if (j == 0) 
                continue;
            if (string[i + 1] == ' ') 
                continue;
        }
        new_string[j] = string[i];
        j++;
    }
    new_string[strlen(new_string) - 1] = '\0';
}

int main(void)
{
    char string[SIZE] = "    hello, i    am  Nikita     ";
    char new_string[SIZE];
    printf("string after: [%s]\n", string);
    remove_extra_spaces(string, new_string);
    printf("string before: [%s]\n", new_string);

    return 0;
}