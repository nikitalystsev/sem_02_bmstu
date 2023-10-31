#include <stdio.h>
#include <math.h>

#define ERR_OK         0
#define ERR_IO         1       
#define ERR_NOT_SQUARE 2

int main(void)
{
    float a, b, c, d;
    int rc = ERR_OK;
	
    setbuf(stdout, NULL);
	
    printf("Enter a, b, c: ");
    if (scanf("%f%f%f", &a, &b, &c) == 3)
    {
        if (a != 0.0)
        {
            d = b * b - 4 * a * c;
            if (d < 0.0)
            {
                printf("There are no real roots\n");
            }
            else if (d > 0)
            {
                printf("x1 = %f, x2 = %f\n", (-b - sqrt(d)) / (2 * a),
                                                (-b + sqrt(d)) / (2 * a));
            }
            else
            {
                printf("x1 = x2 = %f\n", -b / (2 * a));
            }
        }
        else
        {
            rc = ERR_NOT_SQUARE;
            printf("Equation is not square\n");
        }
    }
    else
    {
        rc = ERR_IO;
        printf("I/O error\n");
    }
	
    return rc;
}

