#include <stdio.h>

int main()
{
    int a, k=1;
    printf("number: ");
    scanf("%i", &a);

    for(int i = 0; i < a; i++)
    {
        k = k * (a-i);
    }

    printf("factorial = %i\n", k);
}