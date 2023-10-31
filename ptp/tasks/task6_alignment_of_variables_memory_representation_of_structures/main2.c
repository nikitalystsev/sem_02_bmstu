#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char a = '5';
    short int b = 12;
    unsigned short int c = 15;
    int d = 20;
    unsigned int e = 55;
    long int f = 3000;
    unsigned long int g = 7000;
    long long int h = 15000;
    unsigned long long i = 1000000;
    float j = 20000;
    double k = -200000;
    size_t l = 3000000;

    printf("char:               %c          sizeof(char) = %lu\n", a, sizeof(char));
    printf("short int:          %hi         sizeof(short int) = %lu\n", b, sizeof(short int));
    printf("unsigned short int: %hu         sizeof(unsigned short int) = %lu\n", c, sizeof(unsigned short int));
    printf("int:                %d          sizeof(int) = %lu\n", d, sizeof(int));
    printf("unsigned int:       %u          sizeof(unsigned int) = %lu\n", e, sizeof(unsigned int));
    printf("long int:           %ld         sizeof(long int) = %lu\n", f, sizeof(long int));
    printf("unsigned long int:  %lu         sizeof(unsigned long int) = %lu\n", g, sizeof(unsigned long int));
    printf("long long int:      %lld        sizeof(long long int) = %lu\n", h, sizeof(long long int));
    printf("unsigned long long: %llu        sizeof(unsigned long long) = %lu\n", i, sizeof(unsigned long long));
    printf("float:              %f          sizeof(float) = %lu\n", j, sizeof(float));
    printf("double:             %f          sizeof(double) = %lu\n", k, sizeof(double));
    printf("size_t:             %lu         sizeof(size_t) = %lu\n", l, sizeof(size_t));

    return 0;
}