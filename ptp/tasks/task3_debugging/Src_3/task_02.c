#include <stdio.h>

#define N 5

double get_average(const int a[], size_t n);

int get_max(const int *a, size_t n);

int main()
{
    int arr[N];
    size_t i;

    printf("Enter %d numbers:\n", N);

    for (i = 0; i < N; i++)
    {
        printf("Enter the next number: ");
        if (scanf("%d", &arr[i]) != 1) 
        {
            printf("Input error");
            return 1;
        }
    }

    for (i = 0; i < N; i++)
        printf("Value [%zu] is %d\n", i, arr[i]);

    printf("The average is %g\n", get_average(arr, N));

    printf("The max is %d\n", get_max(arr, N));

    return 0;
}

double get_average(const int a[], size_t n)
{
    double temp = 0.0;

    for (size_t i = 0; i < n; i++)
        temp += a[i];
    temp /= n;

    return temp;
}

int get_max(const int *a, size_t n)
{
    int max = a[0];

    for (size_t i = 1; i < n; i++)
        if (a[i] > max)
            max = a[i];
    return max;
}
