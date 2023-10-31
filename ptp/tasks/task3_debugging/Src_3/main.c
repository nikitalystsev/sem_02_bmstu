#include <stdio.h>

int main(void)
{
    int a[3] = {5, 7, 9};
    int *p = a;
    
    printf("%p   %d\n", p, *p);
    ++p;
    printf("%p   %d", p, *p);    
   
  

    return 0;
}
