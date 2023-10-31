#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STR 128
#define MAX_NUMS 5

#define EXIT_SUCCESS 0
#define ERR_INPUT 1
#define ERR_NO_NUMS 2
#define ERR_TOO_MACH_NUMBERS 3

int input_string(char *string);
int fill_array(char *string, double *array, size_t *arr_len);
double calc_avarage(double *array, size_t arr_len);

int main(void)
{
	char string[MAX_STR];

	int error = input_string(string);
	if (error)
		return error;


	double array[MAX_NUMS];
	size_t arr_len = 0;

	error = fill_array(string, array, &arr_len);
	if (error)
		return error;

	double avarage = calc_avarage(array, arr_len);
	
	printf("%f\n", avarage); 

	return EXIT_SUCCESS;
}	

int input_string(char *string)
{
	char *p = fgets(string, MAX_STR, stdin);
	if (p == NULL)
	{
		printf("Input error\n");
		return ERR_INPUT;
	}

	return EXIT_SUCCESS;
}

int fill_array(char *string, double *array, size_t *arr_len)
{
	char *p = string;
	double num;
	while (*string != '\0')
	{
		num = strtod(string, &p);
		if (p > string)
		{
			if (*arr_len == MAX_NUMS)
			{
				printf("Too much numbers in string\n");
				return ERR_TOO_MACH_NUMBERS;
			}
			array[*arr_len] = num;
			(*arr_len)++;
			string = p;
		}
		else
		{
			string++;
		}
	}

	if (*arr_len == 0)
	{
		printf("Not enough data\n");
		return ERR_NO_NUMS;
	}

	return EXIT_SUCCESS;
}

double calc_avarage(double *array, size_t arr_len)
{
	double sum = 0;
	for (size_t i = 0; i < arr_len; i++)
	{
		sum += array[i];
	}

	double avarage = sum / arr_len;

	return avarage;
}
