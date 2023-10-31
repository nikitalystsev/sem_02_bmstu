#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SIZE 256
#define ERR_INDEX 300


#define ERR_INPUT_STR 1
#define ERR_ALL_STR_ISSPACE 2
#define ERR_LEN_WORD 3

int input_string(char *const string)
{
    char *rc = fgets(string, MAX_SIZE, stdin);
    if (rc == NULL || strlen(string) > MAX_SIZE)
        return ERR_INPUT_STR;
    return EXIT_SUCCESS;
}

int get_pos_by_find_str(char *const find_str, char *const input_str)
{
    int index = 0;

    for (size_t i = 0; i < strlen(input_str); i++)
        if (input_str[i] == find_str[0])
        {
            index = i;
            size_t count = 1;
            i++;
            for (size_t j = 1; j < strlen(find_str); j++)
                if (input_str[i] == find_str[j])
                {
                    i++;
                    count++;
                }
            if (count == strlen(find_str))
                return index;
        }
    return ERR_INDEX;
}

void delete_find_str(char *const input_str, int delete_index, size_t len_find_str)
{
    size_t i = delete_index;
    for (; i < strlen(input_str) - len_find_str + 1; i++)
        input_str[i] = input_str[i + len_find_str];
}

void insert_replace_str(char *const replace_str, char *const input_str, int delete_index)
{
    int i = strlen(input_str);
    for (; i >= delete_index; i--)
        input_str[i + strlen(replace_str)] = input_str[i];
    i = 0;
    for (size_t j = delete_index; j < delete_index + strlen(replace_str); j++)
        input_str[j] = replace_str[i++];
}

int main(void)
{

    char input_str[MAX_SIZE];
    char find_str[MAX_SIZE];
    char replace_str[MAX_SIZE];
    int delete_index;

    input_string(input_str);
    input_string(find_str);
    input_string(replace_str);
    
    input_str[strlen(input_str) - 1] = '\0';
    find_str[strlen(find_str) - 1] = '\0';
    replace_str[strlen(replace_str) - 1] = '\0';

    while ((delete_index = get_pos_by_find_str(find_str, input_str)) != ERR_INDEX)
    {
        delete_find_str(input_str, delete_index, strlen(find_str));
        insert_replace_str(replace_str, input_str, delete_index);
    }

    printf("input_str: %s\n", input_str);

    return 0;
}